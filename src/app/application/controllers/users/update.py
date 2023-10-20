from fastapi import Request

from app.application.controllers import BaseController
from app.application.models import User
from app.application.schemas.users import UserSchema


class UpdateUserController(BaseController):
    def __init__(self, request: Request):
        super(UpdateUserController, self).__init__(request=request, schema=UserSchema)

    async def _call(self):
        await self._parse_request_data()
        self.request_data: UserSchema
        user_id: int = int(self.request.query_params.get("user_id"))
        user: User = await self._get_active_user(user_id=user_id)
        return await self.dump(
            await self._update_user(user=user, name=self.request_data.name)
        )
