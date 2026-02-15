from fastapi import APIRouter, HTTPException
from typing import List, Dict
from loguru import logger

from models.schemas import (
    CharacterModel,
    SceneModel,
    OutlineModel,
    ResponseModel
)

router = APIRouter()


@router.get("/characters")
async def get_characters(
    page: int = 1,
    page_size: int = 10,
    search: str = None
):
    logger.info(f"Getting characters list: page={page}, search={search}")
    
    return ResponseModel(
        code=200,
        data={
            "total": 0,
            "page": page,
            "page_size": page_size,
            "items": []
        }
    )


@router.get("/characters/{name}")
async def get_character(name: str):
    logger.info(f"Getting character: {name}")
    
    return ResponseModel(
        code=200,
        data={}
    )


@router.post("/characters")
async def create_character(character: CharacterModel):
    logger.info(f"Creating character: {character.name}")
    
    return ResponseModel(
        code=200,
        message="创建成功",
        data=character.dict()
    )


@router.put("/characters/{name}")
async def update_character(name: str, character: CharacterModel):
    logger.info(f"Updating character: {name}")
    
    return ResponseModel(
        code=200,
        message="更新成功"
    )


@router.delete("/characters/{name}")
async def delete_character(name: str):
    logger.info(f"Deleting character: {name}")
    
    return ResponseModel(
        code=200,
        message="删除成功"
    )


@router.post("/characters/import")
async def import_characters():
    logger.info("Importing characters")
    
    return ResponseModel(
        code=200,
        message="导入成功"
    )


@router.get("/scenes")
async def get_scenes(
    page: int = 1,
    page_size: int = 10,
    search: str = None
):
    logger.info(f"Getting scenes list: page={page}, search={search}")
    
    return ResponseModel(
        code=200,
        data={
            "total": 0,
            "page": page,
            "page_size": page_size,
            "items": []
        }
    )


@router.get("/scenes/{name}")
async def get_scene(name: str):
    logger.info(f"Getting scene: {name}")
    
    return ResponseModel(
        code=200,
        data={}
    )


@router.post("/scenes")
async def create_scene(scene: SceneModel):
    logger.info(f"Creating scene: {scene.name}")
    
    return ResponseModel(
        code=200,
        message="创建成功",
        data=scene.dict()
    )


@router.put("/scenes/{name}")
async def update_scene(name: str, scene: SceneModel):
    logger.info(f"Updating scene: {name}")
    
    return ResponseModel(
        code=200,
        message="更新成功"
    )


@router.delete("/scenes/{name}")
async def delete_scene(name: str):
    logger.info(f"Deleting scene: {name}")
    
    return ResponseModel(
        code=200,
        message="删除成功"
    )


@router.get("/outlines")
async def get_outlines(
    page: int = 1,
    page_size: int = 10,
    episode_range: str = None
):
    logger.info(f"Getting outlines list: page={page}")
    
    return ResponseModel(
        code=200,
        data={
            "total": 0,
            "page": page,
            "page_size": page_size,
            "items": []
        }
    )


@router.get("/outlines/{episode}")
async def get_outline(episode: int):
    logger.info(f"Getting outline for episode {episode}")
    
    return ResponseModel(
        code=200,
        data={}
    )


@router.post("/outlines")
async def create_outline(outline: OutlineModel):
    logger.info(f"Creating outline for episode {outline.episode}")
    
    return ResponseModel(
        code=200,
        message="创建成功",
        data=outline.dict()
    )


@router.put("/outlines/{episode}")
async def update_outline(episode: int, outline: OutlineModel):
    logger.info(f"Updating outline for episode {episode}")
    
    return ResponseModel(
        code=200,
        message="更新成功"
    )


@router.delete("/outlines/{episode}")
async def delete_outline(episode: int):
    logger.info(f"Deleting outline for episode {episode}")
    
    return ResponseModel(
        code=200,
        message="删除成功"
    )


@router.post("/outlines/import")
async def import_outlines():
    logger.info("Importing outlines")
    
    return ResponseModel(
        code=200,
        message="导入成功"
    )


@router.get("/settings")
async def get_settings():
    logger.info("Getting settings")
    
    return ResponseModel(
        code=200,
        data={}
    )


@router.get("/settings/{key}")
async def get_setting(key: str):
    logger.info(f"Getting setting: {key}")
    
    return ResponseModel(
        code=200,
        data={}
    )


@router.post("/settings")
async def create_setting(key: str, value: str):
    logger.info(f"Creating setting: {key}")
    
    return ResponseModel(
        code=200,
        message="创建成功"
    )


@router.put("/settings/{key}")
async def update_setting(key: str, value: str):
    logger.info(f"Updating setting: {key}")
    
    return ResponseModel(
        code=200,
        message="更新成功"
    )


@router.delete("/settings/{key}")
async def delete_setting(key: str):
    logger.info(f"Deleting setting: {key}")
    
    return ResponseModel(
        code=200,
        message="删除成功"
    )
