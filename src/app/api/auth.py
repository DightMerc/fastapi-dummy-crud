from fastapi import APIRouter, Request
from fastapi.responses import ORJSONResponse

from app.application.controllers.auth.login import LoginAuthController
from app.application.controllers.auth.signup import SignUpAuthController
from app.application.schemas.auth import LoginAuthSchema, SignUpAuthSchema

auth_router = APIRouter()


@auth_router.post("/login")
async def login(request: Request, schema: LoginAuthSchema) -> ORJSONResponse:
    return await LoginAuthController(request=request).call()


@auth_router.post("/signup")
async def signup(request: Request, schema: SignUpAuthSchema) -> ORJSONResponse:
    return await SignUpAuthController(request=request).call()
