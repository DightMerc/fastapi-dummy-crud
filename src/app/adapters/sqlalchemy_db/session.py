import os

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
import sqlalchemy.engine.url as url


def create_session_maker():
    db_uri = url.make_url(os.getenv("DB_URI"))
    if not db_uri:
        raise ValueError("DB_URI env variable is not set")

    engine = create_async_engine(
        db_uri,
        echo=True,
    )
    return async_sessionmaker(engine, autoflush=False, expire_on_commit=False)
