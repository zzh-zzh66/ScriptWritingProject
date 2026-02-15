from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime


class ResponseModel(BaseModel):
    code: int = 200
    message: str = "success"
    data: Optional[Any] = None


class ScriptGenerateRequest(BaseModel):
    episode: int
    creativity_level: float = 0.3
    enable_validation: bool = True


class ScriptBatchGenerateRequest(BaseModel):
    start_episode: int
    end_episode: int
    creativity_level: float = 0.3
    enable_validation: bool = True


class ScriptModel(BaseModel):
    script_id: str
    episode: int
    title: str
    content: str
    word_count: int
    characters: List[str]
    scenes: List[str]
    status: str
    validation_result: Optional[Dict[str, Any]] = None
    created_at: datetime
    updated_at: datetime


class ScriptListResponse(BaseModel):
    total: int
    page: int
    page_size: int
    items: List[ScriptModel]


class BatchProgressModel(BaseModel):
    batch_id: str
    total_episodes: int
    completed_episodes: int
    progress: float
    current_episode: int
    status: str
    episodes: List[Dict[str, Any]]


class CharacterModel(BaseModel):
    name: str
    identity: str
    stages: Dict[str, Dict[str, str]]


class SceneModel(BaseModel):
    name: str
    description: str
    time: str
    type: str


class OutlineModel(BaseModel):
    episode: int
    title: str
    main_progress: str
    event_logic: Dict[str, str]
    hook: str
    climax: str
    highlights: List[str]
    conflicts: List[str]


class ValidationRequest(BaseModel):
    episode: int
    content: str


class ValidationResult(BaseModel):
    is_valid: bool
    issues: List[str]
    warnings: List[str]
    details: Dict[str, Any]


class SystemStatusModel(BaseModel):
    status: str
    uptime: int
    memory_usage: float
    cpu_usage: float
    disk_usage: float
    active_tasks: int
