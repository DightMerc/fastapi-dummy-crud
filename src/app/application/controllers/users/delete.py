from fastapi import Request
from sqlalchemy.ext.asyncio import AsyncSession

from app.application.controllers import BaseController
from app.application.models import User


class DeleteUserController(BaseController):
    def __init__(self, request: Request):
        super(DeleteUserController, self).__init__(request=request)

    async def _call(self):
        async with self.session() as session:
            session: AsyncSession
            session.update
