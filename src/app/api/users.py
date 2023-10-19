from fastapi import APIRouter, Request
from fastapi.responses import ORJSONResponse

from app.application.controllers.users import (
    CreateUserController,
    ListUserController,
    UpdateUserController,
    DeleteUserController,
)

users_router = APIRouter()


@users_router.post("/user")
async def create_user(
    request: Request,
) -> ORJSONResponse:
    return await CreateUserController(request=request).call()


@users_router.get("/user")
async def list_users(
    request: Request,
) -> ORJSONResponse:
    return await ListUserController(request=request).call()


@users_router.put("/user")
async def update_user(
    request: Request,
) -> ORJSONResponse:
    return await UpdateUserController(request=request).call()


@users_router.delete("/user")
async def delete_user(
    request: Request,
) -> ORJSONResponse:
    return await DeleteUserController(request=request).call()
