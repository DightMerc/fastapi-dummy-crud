from fastapi import FastAPI

from app.main.metadata import tags_metadata
from app.main.routers import init_routers
import app.adapters.sqlalchemy_db.models


def create_app() -> FastAPI:

    app = FastAPI(
        title="FastAPI CRUD Dummy Project",
        version="0.0.1",
        contact={
            "name": "Dezir Ibragimov",
            "url": "https://linkedin.com/in/dightmerc",
            "email": "dightmerc@gmail.com",
        },
        openapi_tags=tags_metadata,
    )
    init_routers(app)
    return app
