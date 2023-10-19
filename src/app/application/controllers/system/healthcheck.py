from app.application import BaseController
from fastapi import Request


class HealthcheckController(BaseController):
    def __init__(self, request: Request):
        super(HealthcheckController, self).__init__(request=request)

    async def _call(self):
        return dict()
