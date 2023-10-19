from fastapi import Request

from app.application.controllers import BaseController
from app.application.models import User


class UpdateUserController(BaseController):
    def __init__(self, request: Request):
        super(UpdateUserController, self).__init__(request=request)

    async def _call(self):
        user_id: int = int(self.request.query_params.get("user_id"))
        user: User = await self._get_user(user_id=user_id)

        return self.dump(await self._disable_user(user=user))
