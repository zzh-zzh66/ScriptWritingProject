from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager
import uvicorn
from loguru import logger

from core.config import settings
from core.database import init_db
from api import scripts, documents, validation, system


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting up...")
    await init_db()
    yield
    logger.info("Shutting down...")


app = FastAPI(
    title=settings.PROJECT_NAME,
    description="AI漫剧剧本生成系统API",
    version=settings.VERSION,
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_HOSTS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(scripts.router, prefix="/api/scripts", tags=["scripts"])
app.include_router(documents.router, prefix="/api/documents", tags=["documents"])
app.include_router(validation.router, prefix="/api/validation", tags=["validation"])
app.include_router(system.router, prefix="/api/system", tags=["system"])


@app.get("/")
async def root():
    return {
        "message": "AI漫剧剧本生成系统API",
        "version": settings.VERSION,
        "status": "healthy"
    }


@app.get("/health")
async def health_check():
    return {"status": "healthy"}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG,
        log_level="info"
    )
