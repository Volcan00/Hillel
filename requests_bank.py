import requests
import datetime
from sqlalchemy.orm import Session
import al_db
import models_db

def get_Privatbank_data():
    current_date = datetime.datetime.now().strftime(f"%d.%m.%Y")
    db_date = datetime.datetime.now().strftime(f"%Y-%m-%d")
    r = requests.get(f'https://api.privatbank.ua/p24api/exchange_rates?json&date={current_date}')

    currency_info = r.json()

    saleRate_USD = 0
    purchaseRate_USD = 0

    for c in currency_info['exchangeRate']:
        if c['currency'] == 'USD':
            saleRate_USD = c['saleRate']
            purchaseRate_USD = c['purchaseRate']

    with Session(al_db.engine) as session:
        for c in currency_info['exchangeRate']:
            currency_name = c['currency']
            if c.get('saleRate'):
                print(c)
                saleRate_currency = c['saleRate'] / saleRate_USD
                purchaseRate_currency = c['purchaseRate'] / purchaseRate_USD
                print(f'{currency_name} {saleRate_currency} {purchaseRate_currency }')
                record = models_db.Currency(bank='PrivatBank', 
                                            currency=currency_name, 
                                            date_exchange=db_date, 
                                            buy_rate=purchaseRate_currency, 
                                            sale_rate=saleRate_currency)
                session.add(record)
                session.commit()