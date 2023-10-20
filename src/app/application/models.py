from dataclasses import dataclass


@dataclass
class User:
    id: int
    name: str
    active: bool
    username: str
    password: str
