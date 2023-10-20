import os

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
import sqlalchemy.engine.url as url


def create_session_maker():
    db_uri_env = os.environ.get("DB_URI")
    if not db_uri_env:
        raise ValueError("DB_URI env variable is not set")
    db_uri = url.make_url(db_uri_env)

    engine = create_async_engine(
        db_uri,
        echo=True,
    )
    return async_sessionmaker(engine, autoflush=False, expire_on_commit=False)
