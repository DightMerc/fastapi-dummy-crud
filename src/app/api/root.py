from fastapi import APIRouter

from .system import system_router
from .users import users_router
from .auth import auth_router

root_router = APIRouter()
root_router.include_router(
    system_router,
    prefix="/system",
)
root_router.include_router(users_router, prefix="/users")
root_router.include_router(auth_router, prefix="/auth")
