import logging
from fastapi import Request
from fastapi.responses import ORJSONResponse

from app.main import config


class BaseController(object):
    def __init__(self, request: Request):
        self.logger = logging.getLogger()
        self.request = request

    def _call(self):
        raise NotImplementedError

    def _get_logger(self) -> logging.Logger:
        logger: logging.Logger = logging.getLogger("app")
        logger.setLevel(config.LOG_LEVEL)
        return logger

    async def call(self):
        return ORJSONResponse(await self._call())
