from contextlib import asynccontextmanager
from fastapi import FastAPI
from loguru import logger
from source.api import api_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    FastAPI lifespan context manager.
    """
    logger.info("Application starting up")
    yield
    logger.info("Application shutting down")


app = FastAPI(
    title="My API Framework",
    version="1.0.0",
    description="A production-ready FastAPI service template.",
    lifespan=lifespan
)

app.include_router(
    prefix="/api",
    router=api_router
)