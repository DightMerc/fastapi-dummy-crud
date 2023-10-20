# going to src dir
cd /app/src

# allow migrations
alembic upgrade head

# running tests
#cd /app/src/tests
python -m pytest /app/src/tests
# if tests passed
if [ $? -ne 0 ]
then
    echo '::error::Tests failed. Shutting down.'
else
  # start app
    echo 'All tests passed. Starting application up. 🚀'
  uvicorn app.run:app --port=5060 --host=0.0.0.0
fi

