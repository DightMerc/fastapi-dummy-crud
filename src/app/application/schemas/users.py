from typing import List

from fastapi import Query
from pydantic import BaseModel


class UserSchema(BaseModel):
    name: str


class UserResponseSchema(BaseModel):
    id: int
    name: str
    active: bool
    username: str
