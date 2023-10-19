from typing import List

from fastapi import Request
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.application.controllers import BaseController
from app.application.models import User


class ListUserController(BaseController):
    def __init__(self, request: Request):
        super(ListUserController, self).__init__(request=request)

    async def _call(self):
        return await self._get_active_users()

    async def _get_active_users(self):
        async with self.session() as session:
            session: AsyncSession
            users: List[User] = (
                await session.scalars(select(User).filter(User.active == True))
            ).all()
        return [self.dump(user) for user in users]
