from fastapi import APIRouter
from . import user


api_router = APIRouter()


api_router.include_router(user.user_v1_router, prefix="/v1/users", tags=["v1-users"])