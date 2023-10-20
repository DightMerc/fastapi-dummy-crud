import dataclasses
import logging
from typing import Optional, List

import dataclass_factory
from fastapi import Request, HTTPException
from fastapi.responses import ORJSONResponse
from sqlalchemy import select, update, insert

from app.adapters.sqlalchemy_db.session import create_session_maker
from app.application.models import User


class BaseController(object):
    def __init__(self, request: Request, schema=None):
        self.logger = logging.getLogger()
        self.request = request
        self.session = create_session_maker()
        self.schema = schema

    def _call(self):
        raise NotImplementedError

    async def _parse_request_data(self):
        if not self.schema:
            raise HTTPException(status_code=500, detail="Schema is not specified")
        self.request_data = self.schema(**(await self.request.json()))

    async def dump(self, obj: dataclasses.dataclass):
        factory = dataclass_factory.Factory()
        return factory.dump(obj)

    def _get_logger(self) -> logging.Logger:
        logger: logging.Logger = logging.getLogger("app")
        logger.setLevel(logging.DEBUG)
        return logger

    async def call(self):
        return ORJSONResponse(await self._call())

    async def _get_active_user(self, user_id: int) -> User:
        async with self.session() as session:
            user: Optional[User] = (
                await session.scalars(
                    select(User).filter(User.id == user_id, User.active == True)
                )
            ).first()
            if not user:
                raise HTTPException(status_code=404, detail="User not found")
            return user

    async def _get_users_by_name(self, name: str) -> List[User]:
        async with self.session() as session:
            user: Optional[User] = (
                await session.scalars(
                    select(User).filter(User.name == name, User.active == True)
                )
            ).all()
            if not user:
                raise HTTPException(status_code=404, detail="User not found")
            return user

    async def _disable_user(self, user: User) -> User:
        async with self.session() as session:
            query = update(User).where(User.id == user.id).values(active=False)
            await session.execute(query)
            await session.commit()
        return user

    async def _update_user(self, user: User, name: str) -> User:
        user.name = name
        async with self.session() as session:
            query = update(User).where(User.id == user.id).values(name=name)
            await session.execute(query)
            await session.commit()
        return user

    async def _create_user(self, name: str) -> User:
        async with self.session() as session:
            query = insert(User).values(name=name, active=True)
            result = await session.execute(query)
            await session.commit()
        user_id: int = result.inserted_primary_key[0]
        return await self._get_active_user(user_id=user_id)
