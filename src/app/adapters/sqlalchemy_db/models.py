from sqlalchemy import Integer, String, Column, MetaData, Table, Boolean
from sqlalchemy.orm import registry

from app.application.models import User

metadata_obj = MetaData()
mapper_registry = registry()

user = Table(
    "users",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("name", String()),
    Column("active", Boolean()),
)

mapper_registry.map_imperatively(User, user)
