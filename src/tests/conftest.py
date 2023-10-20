import os
import shutil

import pytest
import sqlalchemy
from fastapi.testclient import TestClient


@pytest.fixture()
def client():
    os.environ["DB_URI"] = "sqlite+aiosqlite:////app/src/tests/test.db"
    os.environ["JWT_SECRET_KEY"] = "top_secret"
    os.environ["JWT_REFRESH_SECRET_KEY"] = "top_top_secret"
    from app.main import app

    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture()
def db():
    shutil.copy(
        os.path.join(os.path.abspath(os.getcwd()), "tests/test.template.db"),
        os.path.join(os.path.abspath(os.getcwd()), "tests/test.db"),
    )
    yield
    os.remove(os.path.join(os.path.abspath(os.getcwd()), "tests/test.db"))
