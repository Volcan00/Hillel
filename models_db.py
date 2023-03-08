from sqlalchemy import Column, Integer, String, Float
from al_db import Base

class Currency(Base):
    __tablename__ = 'currency'
    id = Column(Integer, primary_key = True, unique = True)
    bank = Column(String(50))
    currency = Column(String(120))
    date_exchange = Column(String(120))
    buy_rate = Column(Float)
    sale_rate = Column(Float)

    def __init__(self, bank, currency, date_exchange, buy_rate, sale_rate):
        self.bank = bank
        self.currency = currency
        self.date_exchange = date_exchange
        self.buy_rate = buy_rate
        self.sale_rate = sale_rate

    def __repr__(self):
        return f'User {self.bank!r}'

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key = True, unique = True)
    username = Column(String(50))
    password = Column(String(120))
    email = Column(String(120))
    first_name = Column(String(50))
    surname = Column(String(50))
    tax_id = Column(Integer, default = None)
    avatar_link = Column(String(120), default = None)

    def __init__(self, username, password, email = None, first_name = None, surname = None, tax_id = None, avatar_link = None):
        self.username = username
        self.password = password
        self.email = email
        self.first_name = first_name
        self.surname = surname
        if tax_id is not None:
            self.tax_id = tax_id
        else:
            raise Exception('User has no tax id')
        self.avatar_link = avatar_link

    def get_taxes_info(self):
        if self.tax_id is None:
            raise Exception("User has no tax id")
        else:
            return "tac_id is filled"

    def __repr__(self):
        return f"User{self.username!r}" 