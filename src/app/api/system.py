from fastapi import APIRouter, Request
from fastapi.responses import ORJSONResponse

from app.application.controllers.system.healthcheck import HealthcheckController

system_router = APIRouter()


@system_router.get("/healthcheck")
async def healthcheck(
    request: Request,
) -> ORJSONResponse:
    return await HealthcheckController(request=request).call()
