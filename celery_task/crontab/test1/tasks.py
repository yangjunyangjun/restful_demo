import datetime
from celery_task.main import app


@app.task
def test():
    print(datetime.datetime.now())
