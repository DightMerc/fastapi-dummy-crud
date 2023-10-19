from app.application import BaseController
from fastapi import Request


class UpdateUserController(BaseController):
    def __init__(self, request: Request):
        super(UpdateUserController, self).__init__(request=request)

    async def _call(self):
        return dict()
