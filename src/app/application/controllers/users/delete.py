from app.application import BaseController
from fastapi import Request


class DeleteUserController(BaseController):
    def __init__(self, request: Request):
        super(DeleteUserController, self).__init__(request=request)

    async def _call(self):
        return dict()
