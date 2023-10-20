from typing import Annotated, Union, List

from fastapi import APIRouter, Request, Depends, Query
from fastapi.responses import ORJSONResponse

from app.application.controllers.users import (
    CreateUserController,
    ListUserController,
    UpdateUserController,
    DeleteUserController,
)
from app.application.schemas.users import (
    UserSchema,
    UserResponseSchema,
)
from app.main.di import auth_required

users_router = APIRouter()


@users_router.post("/user", tags=["users"], response_model=UserResponseSchema)
async def create_user(
    request: Request,
    auth=Depends(auth_required),
) -> ORJSONResponse:
    """
    User Create endpoint. Creates new user record in database
    """
    return await CreateUserController(request=request).call()


@users_router.get("/user", tags=["users"], response_model=List[UserResponseSchema])
async def list_users(
    request: Request,
    auth=Depends(auth_required),
    user_id: Annotated[Union[str, None], Query(description="User ID")] = None,
    name: Annotated[Union[str, None], Query(description="Users name")] = None,
) -> ORJSONResponse:
    """
    User List endpoint. Accepts query params: user_id, name.
    """
    return await ListUserController(request=request).call()


@users_router.put("/user", tags=["users"], response_model=UserResponseSchema)
async def update_user(
    request: Request,
    schema: UserSchema,
    auth=Depends(auth_required),
) -> ORJSONResponse:
    """
    User Update endpoint. Updates user`s name
    """
    return await UpdateUserController(request=request).call()


@users_router.delete("/user", tags=["users"], response_model=UserResponseSchema)
async def delete_user(
    request: Request,
    auth=Depends(auth_required),
) -> ORJSONResponse:
    """
    User Delete endpoint. Deactivates user
    """
    return await DeleteUserController(request=request).call()
