from fastapi import APIRouter, Depends, HTTPException, WebSocket, WebSocketDisconnect
from typing import List
from datetime import datetime
import uuid
import asyncio
from loguru import logger

from models.schemas import (
    ScriptGenerateRequest,
    ScriptBatchGenerateRequest,
    ScriptModel,
    ScriptListResponse,
    BatchProgressModel,
    ResponseModel
)
from services.script_service import script_service

router = APIRouter()


class ConnectionManager:
    def __init__(self):
        self.active_connections: dict[str, List[WebSocket]] = {}

    async def connect(self, websocket: WebSocket, batch_id: str):
        await websocket.accept()
        if batch_id not in self.active_connections:
            self.active_connections[batch_id] = []
        self.active_connections[batch_id].append(websocket)

    def disconnect(self, websocket: WebSocket, batch_id: str):
        if batch_id in self.active_connections:
            self.active_connections[batch_id].remove(websocket)
            if not self.active_connections[batch_id]:
                del self.active_connections[batch_id]

    async def broadcast(self, batch_id: str, message: dict):
        if batch_id in self.active_connections:
            for connection in self.active_connections[batch_id]:
                try:
                    await connection.send_json(message)
                except:
                    pass


manager = ConnectionManager()


batch_tasks: dict[str, dict] = {}


@router.post("/generate", response_model=ResponseModel)
async def generate_script(request: ScriptGenerateRequest):
    logger.info(f"Generating script for episode {request.episode}")
    
    try:
        script_content = await _generate_single_script(
            request.episode,
            request.creativity_level,
            request.enable_validation
        )
        
        word_count = len(script_content)
        
        script = ScriptModel(
            script_id=f"script_{uuid.uuid4().hex[:8]}",
            episode=request.episode,
            title=f"第{request.episode}集",
            content=script_content,
            word_count=word_count,
            characters=[],
            scenes=[],
            status="completed",
            validation_result={"is_valid": True, "issues": []},
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        
        return ResponseModel(
            code=200,
            message="生成成功",
            data=script.dict()
        )
    except Exception as e:
        logger.error(f"Error generating script: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/generate-batch", response_model=ResponseModel)
async def generate_batch_scripts(request: ScriptBatchGenerateRequest):
    logger.info(f"Generating batch scripts from episode {request.start_episode} to {request.end_episode}")
    
    batch_id = f"batch_{uuid.uuid4().hex[:8]}"
    
    batch_tasks[batch_id] = {
        "batch_id": batch_id,
        "total_episodes": request.end_episode - request.start_episode + 1,
        "completed_episodes": 0,
        "progress": 0,
        "current_episode": request.start_episode,
        "status": "processing",
        "episodes": []
    }
    
    asyncio.create_task(
        _process_batch_generation(
            batch_id,
            request.start_episode,
            request.end_episode,
            request.creativity_level,
            request.enable_validation
        )
    )
    
    return ResponseModel(
        code=200,
        message="批量生成任务已创建",
        data=batch_tasks[batch_id]
    )


@router.get("/progress/{batch_id}", response_model=ResponseModel)
async def get_batch_progress(batch_id: str):
    if batch_id not in batch_tasks:
        raise HTTPException(status_code=404, detail="批次不存在")
    
    return ResponseModel(
        code=200,
        data=batch_tasks[batch_id]
    )


@router.websocket("/progress/ws/{batch_id}")
async def websocket_progress(websocket: WebSocket, batch_id: str):
    await manager.connect(websocket, batch_id)
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        manager.disconnect(websocket, batch_id)


@router.get("/", response_model=ScriptListResponse)
async def get_scripts(
    page: int = 1,
    page_size: int = 10,
    episode: int = None,
    status: str = None
):
    logger.info(f"Getting scripts list: page={page}, page_size={page_size}")
    
    return ScriptListResponse(
        total=0,
        page=page,
        page_size=page_size,
        items=[]
    )


@router.get("/{episode}", response_model=ResponseModel)
async def get_script(episode: int):
    logger.info(f"Getting script for episode {episode}")
    
    return ResponseModel(
        code=200,
        data={
            "script_id": f"script_{episode}",
            "episode": episode,
            "title": f"第{episode}集",
            "content": "",
            "word_count": 0,
            "characters": [],
            "scenes": [],
            "status": "completed",
            "validation_result": {"is_valid": True, "issues": []},
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        }
    )


@router.put("/{episode}", response_model=ResponseModel)
async def update_script(episode: int, content: str):
    logger.info(f"Updating script for episode {episode}")
    
    return ResponseModel(
        code=200,
        message="更新成功"
    )


@router.get("/{episode}/export")
async def export_script(episode: int, format: str = "markdown"):
    logger.info(f"Exporting script for episode {episode} in format {format}")
    
    return {
        "message": "导出成功",
        "format": format,
        "content": ""
    }


@router.get("/{episode}/history")
async def get_script_history(episode: int):
    logger.info(f"Getting history for episode {episode}")
    
    return {
        "history": []
    }


async def _generate_single_script(episode: int, creativity_level: float, enable_validation: bool) -> str:
    return await script_service.generate_single_script(episode, creativity_level, enable_validation)


async def _process_batch_generation(
    batch_id: str,
    start_episode: int,
    end_episode: int,
    creativity_level: float,
    enable_validation: bool
):
    task = batch_tasks[batch_id]
    
    for episode in range(start_episode, end_episode + 1):
        task["current_episode"] = episode
        
        try:
            script_content = await _generate_single_script(episode, creativity_level, enable_validation)
            word_count = len(script_content)
            
            episode_data = {
                "episode": episode,
                "status": "completed",
                "word_count": word_count
            }
            task["episodes"].append(episode_data)
            task["completed_episodes"] += 1
            task["progress"] = (task["completed_episodes"] / task["total_episodes"]) * 100
            
            await manager.broadcast(batch_id, {
                "type": "progress",
                "data": task
            })
            
        except Exception as e:
            logger.error(f"Error generating episode {episode}: {e}")
            task["episodes"].append({
                "episode": episode,
                "status": "failed",
                "error": str(e)
            })
    
    task["status"] = "completed"
    await manager.broadcast(batch_id, {
        "type": "completed",
        "data": task
    })
