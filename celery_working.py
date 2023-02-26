from celery import Celery
import datetime
import os
import models_db
import al_db
from sqlalchemy.orm import Session
import requests_bank

rabbit_host = os.environ.get('RABBIT_HOST', 'localhost')
app = Celery('celery_working', broker=f"pyamqp://guest@{rabbit_host}//")

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(300.0, get_bank_data_task.s(), name="add every 300 seconds")

@app.task
# def add(x, y):
#     print(x + y)
#     record_1 = models_db.Currency(bank = "GGG", currency = "USD", date_exchange = "2023-02-19", buy_rate = 36.6, sale_rate = 37.45)
#     with Session(al_db.engine) as session:
#             session.add(record_1)
#             session.commit()

# add(1,2)
def get_bank_data_task():
    requests_bank.get_Privatbank_data()
    return True