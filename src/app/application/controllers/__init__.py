import dataclasses
import logging
from typing import Optional

import dataclass_factory
from fastapi import Request, HTTPException
from fastapi.responses import ORJSONResponse
from sqlalchemy import select, update

from app.adapters.sqlalchemy_db.session import create_session_maker
from app.application.models import User


class BaseController(object):
    def __init__(self, request: Request):
        self.logger = logging.getLogger()
        self.request = request
        self.session = create_session_maker()

    def _call(self):
        raise NotImplementedError

    def dump(self, obj: dataclasses.dataclass):
        factory = dataclass_factory.Factory()
        return factory.dump(obj)

    def _get_logger(self) -> logging.Logger:
        logger: logging.Logger = logging.getLogger("app")
        logger.setLevel(logging.DEBUG)
        return logger

    async def call(self):
        return ORJSONResponse(await self._call())

    async def _get_user(self, user_id: int) -> User:
        async with self.session() as session:
            user: Optional[User] = (
                await session.scalars(
                    select(User).filter(User.id == user_id, User.active == True)
                )
            ).first()
            if not user:
                raise HTTPException(status_code=404, detail="User not found")
            return user

    async def _disable_user(self, user: User) -> User:
        async with self.session() as session:
            query = update(User).where(User.id == user.id).values(active=False)
            await session.execute(query)
            await session.commit()
        return user
