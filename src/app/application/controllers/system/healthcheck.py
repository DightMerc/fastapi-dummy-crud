from fastapi import Request
from sqlalchemy import text

from app.application.controllers import BaseController


class HealthcheckController(BaseController):
    def __init__(self, request: Request):
        super(HealthcheckController, self).__init__(request=request)

    async def _call(self):
        async with self.session() as session:
            await session.execute(text("select 1;"))
        return dict(status="Ok")
