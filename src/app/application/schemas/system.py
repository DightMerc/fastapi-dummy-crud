from pydantic import BaseModel


class HealthcheckResponseSchema(BaseModel):
    status: str
