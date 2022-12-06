import sqlite3
import datetime

class DBManager():
    def __enter__(self):
        self.con = sqlite3.connect("currency.db")
        self.cursor = self.con.cursor()
        return self
    
    def __exit__(self):
        self.cursor.close()
        self.con.close()

    def get_result(self, query):
        res_1 = self.cursor.execute(query)
        result = res_1.fetchone()
        return result

    def write_data(self, query):
        self.cursor.execute(query)
        self.con.commit()

def generate_data():
    data = [ 
        {'bank': 'Privatbank', 'date_exchange': '2022-11-25', 'currency': "UAH", 'buy_rate': 0.025, 'sell_rate': 0.03},
        {'bank': 'Privatbank', 'date_exchange': '2022-11-25', 'currency': "EUR", 'buy_rate': 0.095, 'sell_rate': 0.097},
        {'bank': 'Privatbank', 'date_exchange': '2022-11-25', 'currency': "USD", 'buy_rate': 1, 'sell_rate': 1},
        {'bank': 'Privatbank', 'date_exchange': '2022-11-25', 'currency': "GBP", 'buy_rate': 1.16, 'sell_rate': 1.6},
        ]
        # date_exchange = datetime.datetime.now().strftime('%Y-%m-%d')
    with DBManager() as db:
        for bank_info in data:
            query = "INSERT INTO currency (bank, currency, date_exchange, buy_rate, sale_rate) VALUES ('{bank}', '{currency}', '{date_exchange}', '{buy_rate}', '{sell_rate}')".format(**bank_info)
            db.write_data(query)