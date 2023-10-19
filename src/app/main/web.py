from fastapi import FastAPI

from app.main.routers import init_routers


def create_app() -> FastAPI:
    app = FastAPI()
    init_routers(app)
    return app
