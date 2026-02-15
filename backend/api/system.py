from fastapi import APIRouter, HTTPException
from loguru import logger
import time
import psutil

from models.schemas import ResponseModel

router = APIRouter()

start_time = time.time()


@router.get("/config", response_model=ResponseModel)
async def get_config():
    logger.info("Getting config")
    
    return ResponseModel(
        code=200,
        data={}
    )


@router.put("/config", response_model=ResponseModel)
async def update_config():
    logger.info("Updating config")
    
    return ResponseModel(
        code=200,
        message="更新成功"
    )


@router.post("/config/reset", response_model=ResponseModel)
async def reset_config():
    logger.info("Resetting config")
    
    return ResponseModel(
        code=200,
        message="重置成功"
    )


@router.get("/status", response_model=ResponseModel)
async def get_system_status():
    logger.info("Getting system status")
    
    uptime = int(time.time() - start_time)
    memory = psutil.virtual_memory()
    cpu = psutil.cpu_percent(interval=1)
    disk = psutil.disk_usage('/')
    
    return ResponseModel(
        code=200,
        data={
            "status": "healthy",
            "uptime": uptime,
            "memory_usage": round(memory.used / (1024 ** 3), 2),
            "cpu_usage": cpu,
            "disk_usage": round(disk.percent, 2),
            "active_tasks": 0
        }
    )


@router.get("/tasks", response_model=ResponseModel)
async def get_tasks():
    logger.info("Getting tasks")
    
    return ResponseModel(
        code=200,
        data=[]
    )


@router.get("/logs", response_model=ResponseModel)
async def get_logs(
    page: int = 1,
    page_size: int = 100,
    level: str = None
):
    logger.info(f"Getting logs: page={page}, level={level}")
    
    return ResponseModel(
        code=200,
        data={
            "total": 0,
            "page": page,
            "page_size": page_size,
            "items": []
        }
    )


@router.get("/logs/export")
async def export_logs():
    logger.info("Exporting logs")
    
    return {
        "message": "导出成功",
        "content": ""
    }


@router.get("/users", response_model=ResponseModel)
async def get_users(
    page: int = 1,
    page_size: int = 10
):
    logger.info(f"Getting users list: page={page}")
    
    return ResponseModel(
        code=200,
        data={
            "total": 0,
            "page": page,
            "page_size": page_size,
            "items": []
        }
    )


@router.post("/users", response_model=ResponseModel)
async def create_user():
    logger.info("Creating user")
    
    return ResponseModel(
        code=200,
        message="创建成功"
    )


@router.put("/users/{user_id}", response_model=ResponseModel)
async def update_user(user_id: int):
    logger.info(f"Updating user: {user_id}")
    
    return ResponseModel(
        code=200,
        message="更新成功"
    )


@router.delete("/users/{user_id}", response_model=ResponseModel)
async def delete_user(user_id: int):
    logger.info(f"Deleting user: {user_id}")
    
    return ResponseModel(
        code=200,
        message="删除成功"
    )


@router.post("/users/{user_id}/password", response_model=ResponseModel)
async def change_password(user_id: int):
    logger.info(f"Changing password for user: {user_id}")
    
    return ResponseModel(
        code=200,
        message="密码修改成功"
    )
