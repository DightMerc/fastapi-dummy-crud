from fastapi import FastAPI

from app.main.routers import init_routers
import app.adapters.sqlalchemy_db.models


def create_app() -> FastAPI:
    app = FastAPI()
    init_routers(app)
    return app
