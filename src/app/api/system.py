from fastapi import APIRouter, Request
from fastapi.responses import ORJSONResponse

from app.application.controllers.system import HealthcheckController
from app.application.schemas.system import HealthcheckResponseSchema

system_router = APIRouter()


@system_router.get(
    "/healthcheck", tags=["system"], response_model=HealthcheckResponseSchema
)
async def healthcheck(
    request: Request,
) -> ORJSONResponse:
    """
    Healthcheck API endpoint. For Docker healthcheck. Calls database
    """
    return await HealthcheckController(request=request).call()
