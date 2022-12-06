from flask import Flask, render_template
from requests import request 
from db_manager import *

app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def login_user():
    if request.method == 'GET':
        return "OK"
    if request.method == 'POST':
        return "OK"
    return "<p>Login!</p>"

@app.route("/logout", methods = ['GET'])
def logout_user():
    if request.method == 'GET':
        return "OK"
    return "<p>Logout</p>"

@app.route("/register", methods = ['GET', 'POST'])
def register_user():
    if request.method == 'GET':
        return "OK"
    if request.method == 'POST':
        return "OK"
    return "Registration form"

@app.route("/user_page", methods = ['GET'])
def user_access():
    if request.method == 'POST':
        return "OK"
    return "More functions"

@app.route("/currency", methods = ['GET', 'POST'])
def currency_convert():
    # currency = [

    #     {'bank': 'Privatbank', 'date': '2022-11-25', 'currency_name': "UAH", 'buy_rate': 0.025, 'sell_rate': 0.03},
    #     {'bank': 'Privatbank', 'date': '2022-11-25', 'currency_name': "EUR", 'buy_rate': 0.095, 'sell_rate': 0.097},
    #     {'bank': 'Privatbank', 'date': '2022-11-25', 'currency_name': "USD", 'buy_rate': 1, 'sell_rate': 1},
    #     {'bank': 'Privatbank', 'date': '2022-11-25', 'currency_name': "GBP", 'buy_rate': 1.16, 'sell_rate': 1.6},

    #     {'bank': 'Monobank', 'date': '2022-11-25', 'currency_name': "UAH", 'buy_rate': 0.026, 'sell_rate': 0.02},
    #     {'bank': 'Monobank', 'date': '2022-11-25', 'currency_name': "EUR", 'buy_rate': 0.09, 'sell_rate': 0.095},
    #     {'bank': 'Monobank', 'date': '2022-11-25', 'currency_name': "USD", 'buy_rate': 1, 'sell_rate': 1},
    #     {'bank': 'Monobank', 'date': '2022-11-25', 'currency_name': "GBP", 'buy_rate': 1.15, 'sell_rate': 1.2}
        
    #     ]

    con = sqlite3.connect("currency.db")
    cursor = con.cursor()
    if request.method == 'POST':
        user_bank = request.form['bank']
        user_currency_1 = request.form['currency_1']
        user_date = request.form['date']
        user_currency_2 = request.form['currency_2']
        res_1 = cursor.execute(f'SELECT buy_rate, sale_rate FROM currency WHERE bank = "{user_bank}" and date_exchange = "{user_date}" and currency = "{user_currency_1}"')
        buy_rate_1, sale_rate_1 = res_1.fetchone()
        res_2 = cursor.execute(f'SELECT buy_rate, sale_rate FROM currency WHERE bank = "{user_bank}" and date_exchange = "{user_date}" and currency = "{user_curency_2}"')
        buy_rate_2, sale_rate_2 = res_2.fetchone()

        cur_exchange_buy = buy_rate_2 / buy_rate_1
        cur_exchange_sale = sale_rate_2 / sale_rate_1

        cursor.close()
        con.close()

        return render_template('data_form.html', cur_exchange_buy = cur_exchange_buy, cur_exchange_sale = cur_exchange_sale, user_currency_1 = user_currency_1, user_currency_2 = user_currency_2)
    else:
        return render_template(data_form.html)