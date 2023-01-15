from celery import Celery
import datetime
import os

rabbit_host = os.environ.get('RABBIT_HOST', 'localhost')
app = Celery('celery_working', broker=f"pyamqp://guest@{rabbit_host}//")

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(300.0, add.s(x = 2, y = 3), name="add every 300 seconds")

@app.task
def add(x, y):
    print(x + y)
    with open("test.txt", "w") as f:
        f.write(f'x + y = {x+y} {datetime.datetime.now()}')
    return x + y

add(1,2)