from fastapi import Request

from app.application.controllers import BaseController
from app.application.schemas.users import UserSchema


class CreateUserController(BaseController):
    def __init__(self, request: Request):
        super(CreateUserController, self).__init__(request=request, schema=UserSchema)

    async def _call(self):
        await self._parse_request_data()
        self.request_data: UserSchema
        return await self.dump(await self._create_user(name=self.request_data.name))
