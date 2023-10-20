from fastapi import APIRouter, Request
from fastapi.responses import ORJSONResponse

from app.application.controllers.auth.login import LoginAuthController
from app.application.controllers.auth.signup import SignUpAuthController
from app.application.schemas.auth import (
    LoginAuthSchema,
    SignUpAuthSchema,
    LoginResponseSchema,
)
from app.application.schemas.users import UserResponseSchema

auth_router = APIRouter()


@auth_router.post("/login", tags=["auth"], response_model=LoginResponseSchema)
async def login(request: Request, schema: LoginAuthSchema) -> ORJSONResponse:
    return await LoginAuthController(request=request).call()


@auth_router.post("/signup", tags=["auth"], response_model=UserResponseSchema)
async def signup(request: Request, schema: SignUpAuthSchema) -> ORJSONResponse:
    return await SignUpAuthController(request=request).call()
