from fastapi import APIRouter, Request
from fastapi.responses import ORJSONResponse

system_router = APIRouter()


@system_router.get("/healthcheck")
async def healthcheck(
    request: Request,
) -> ORJSONResponse:
    return ORJSONResponse(dict())
