from app.application import BaseController
from fastapi import Request


class ListUserController(BaseController):
    def __init__(self, request: Request):
        super(ListUserController, self).__init__(request=request)

    async def _call(self):
        return dict()
