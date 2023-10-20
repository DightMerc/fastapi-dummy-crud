# going to src dir
cd /app/src

# allow migrations
alembic upgrade head

# start app
uvicorn app.run:app --port=5060 --host=0.0.0.0