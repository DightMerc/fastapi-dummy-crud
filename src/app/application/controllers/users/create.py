from app.application import BaseController
from fastapi import Request


class CreateUserController(BaseController):
    def __init__(self, request: Request):
        super(CreateUserController, self).__init__(request=request)

    async def _call(self):
        return dict()
