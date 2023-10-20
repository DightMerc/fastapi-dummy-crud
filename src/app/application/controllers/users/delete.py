from fastapi import Request

from app.application.controllers import BaseController
from app.application.models import User


class DeleteUserController(BaseController):
    def __init__(self, request: Request):
        super(DeleteUserController, self).__init__(request=request)

    async def _call(self):
        user_id: int = int(self.request.query_params.get("user_id"))
        user: User = await self._get_active_user(user_id=user_id)

        return await self.dump(await self._disable_user(user=user))
