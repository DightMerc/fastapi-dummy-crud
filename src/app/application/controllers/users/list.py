from typing import List, Dict

from fastapi import Request, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.application.controllers import BaseController
from app.application.models import User


class ListUserController(BaseController):
    def __init__(self, request: Request):
        super(ListUserController, self).__init__(request=request)

    async def _call(self):
        if not self.request.query_params:
            return await self._get_active_users()
        if self.request.query_params.get("user_id"):
            user_id: str = self.request.query_params.get("user_id")
            if not user_id.isdigit():
                raise HTTPException(status_code=400, detail="Id must be int")
            return [await self.dump(await self._get_active_user(user_id=int(user_id)))]
        if self.request.query_params.get("name"):
            name: str = self.request.query_params.get("name")
            users: List[User] = await self._get_users_by_name(name=name)
            return [await self.dump(user) for user in users]

    async def _get_active_users(self) -> List[Dict]:
        async with self.session() as session:
            session: AsyncSession
            users: List[User] = (
                await session.scalars(select(User).filter(User.active == True))
            ).all()
        return [await self.dump(user) for user in users]
