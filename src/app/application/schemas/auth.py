from pydantic import BaseModel


class LoginAuthSchema(BaseModel):
    username: str
    password: str


class SignUpAuthSchema(BaseModel):
    username: str
    password: str


class TokenPayload(BaseModel):
    exp: int
    sub: str
