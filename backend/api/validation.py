from fastapi import APIRouter, HTTPException
from loguru import logger

from models.schemas import ValidationRequest, ValidationResult, ResponseModel

router = APIRouter()


@router.post("/consistency", response_model=ResponseModel)
async def validate_consistency(request: ValidationRequest):
    logger.info(f"Validating consistency for episode {request.episode}")
    
    result = ValidationResult(
        is_valid=True,
        issues=[],
        warnings=[],
        details={
            "character_consistency": {
                "is_valid": True,
                "issues": []
            },
            "ability_consistency": {
                "is_valid": True,
                "issues": []
            },
            "force_consistency": {
                "is_valid": True,
                "issues": []
            }
        }
    )
    
    return ResponseModel(
        code=200,
        data=result.dict()
    )


@router.post("/format", response_model=ResponseModel)
async def validate_format(request: ValidationRequest):
    logger.info(f"Validating format for episode {request.episode}")
    
    result = ValidationResult(
        is_valid=True,
        issues=[],
        warnings=[],
        details={}
    )
    
    return ResponseModel(
        code=200,
        data=result.dict()
    )


@router.post("/rules", response_model=ResponseModel)
async def validate_rules(request: ValidationRequest):
    logger.info(f"Validating rules for episode {request.episode}")
    
    result = ValidationResult(
        is_valid=True,
        issues=[],
        warnings=[],
        details={}
    )
    
    return ResponseModel(
        code=200,
        data=result.dict()
    )


@router.post("/batch", response_model=ResponseModel)
async def validate_batch(start_episode: int, end_episode: int):
    logger.info(f"Validating batch from episode {start_episode} to {end_episode}")
    
    return ResponseModel(
        code=200,
        data={
            "total_episodes": end_episode - start_episode + 1,
            "valid_episodes": 0,
            "invalid_episodes": 0,
            "results": []
        }
    )
