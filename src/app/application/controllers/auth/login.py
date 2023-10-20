from fastapi import Request, HTTPException
from starlette import status

from app.application.controllers import BaseController
from app.application.models import User
from app.application.schemas.auth import LoginAuthSchema
from app.main.security import verify_password, create_access_token, create_refresh_token


class LoginAuthController(BaseController):
    def __init__(self, request: Request):
        super(LoginAuthController, self).__init__(
            request=request, schema=LoginAuthSchema
        )

    async def _call(self):
        await self._parse_request_data()
        self.request_data: LoginAuthSchema
        user: User = await self._get_user_by_username(
            username=self.request_data.username
        )
        if not (await verify_password(self.request_data.password, user.password)):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Incorrect email or password",
            )
        return dict(
            access_token=(await create_access_token(user.username)),
            refresh_token=(await create_refresh_token(user.username)),
        )
