from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    PROJECT_NAME: str = "AI漫剧剧本生成系统"
    VERSION: str = "1.0.0"
    DEBUG: bool = True
    
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    
    ALLOWED_HOSTS: List[str] = ["*"]
    
    DATABASE_URL: str = "sqlite:///./backend/data/database.db"
    
    REDIS_URL: str = "redis://localhost:6379/0"
    
    SECRET_KEY: str = "your-secret-key-here"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    LOG_LEVEL: str = "INFO"
    
    MAX_UPLOAD_SIZE: int = 10 * 1024 * 1024  # 10MB
    
    CREATIVITY_LEVEL_MIN: float = 0.0
    CREATIVITY_LEVEL_MAX: float = 1.0
    
    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
