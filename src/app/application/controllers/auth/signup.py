from typing import Optional

from fastapi import Request, HTTPException
from starlette import status

from app.application.controllers import BaseController
from app.application.models import User
from app.application.schemas.auth import SignUpAuthSchema
from app.main.security import (
    get_hashed_password,
)


class SignUpAuthController(BaseController):
    def __init__(self, request: Request):
        super(SignUpAuthController, self).__init__(
            request=request, schema=SignUpAuthSchema
        )

    async def _call(self):
        await self._parse_request_data()
        self.request_data: SignUpAuthSchema
        possible_user: Optional[User] = await self._get_possible_user_by_username(
            username=self.request_data.username
        )
        if possible_user:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"User with username '{self.request_data.username}' already exists",
            )
        user: User = await self._create_new_auth_user(
            username=self.request_data.username,
            password=await get_hashed_password(self.request_data.password),
        )
        return await self.dump(user)
