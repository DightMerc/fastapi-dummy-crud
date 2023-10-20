from fastapi import APIRouter, Request, Depends
from fastapi.responses import ORJSONResponse

from app.application.controllers.users import (
    CreateUserController,
    ListUserController,
    UpdateUserController,
    DeleteUserController,
)
from app.application.models import User
from app.application.schemas.users import UserSchema
from app.main.di import get_current_user

users_router = APIRouter()


@users_router.post("/user")
async def create_user(
    request: Request, username: str = Depends(get_current_user)
) -> ORJSONResponse:
    return await CreateUserController(request=request).call()


@users_router.get("/user")
async def list_users(
    request: Request, username: str = Depends(get_current_user)
) -> ORJSONResponse:
    return await ListUserController(request=request).call()


@users_router.put("/user")
async def update_user(
    request: Request,
    schema: UserSchema,
    username: str = Depends(get_current_user),
) -> ORJSONResponse:
    return await UpdateUserController(request=request).call()


@users_router.delete("/user")
async def delete_user(
    request: Request, username: str = Depends(get_current_user)
) -> ORJSONResponse:
    return await DeleteUserController(request=request).call()
