from contextlib import asynccontextmanager
from fastapi import FastAPI
from loguru import logger



app = FastAPI()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    FastAPI lifespan context manager.
    """
    logger.info("Application starting up")
    yield
    logger.info("Application shutting down")


app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0",
    description="A production-ready FastAPI service template.",
    lifespan=lifespan
)
