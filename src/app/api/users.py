from fastapi import APIRouter, Request
from fastapi.responses import ORJSONResponse

users_router = APIRouter()


@users_router.post("/user")
def create_user(
    request: Request,
) -> ORJSONResponse:
    return ORJSONResponse(dict())


@users_router.get("/user")
def list_users(
    request: Request,
) -> ORJSONResponse:
    return ORJSONResponse(dict())


@users_router.put("/user")
def update_user(
    request: Request,
) -> ORJSONResponse:
    return ORJSONResponse(dict())


@users_router.delete("/user")
def delete_user(
    request: Request,
) -> ORJSONResponse:
    return ORJSONResponse(dict())
