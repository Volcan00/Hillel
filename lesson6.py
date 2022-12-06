from flask import Flask, render_template, request
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
    if request.method == 'POST':
        user_bank = request.form['bank']
        user_currency_1 = request.form['currency_1']
        user_date = request.form['date']
        user_currency_2 = request.form['currency_2']

        with DBManager() as db:
            db.generate_data()
            buy_rate_1, sale_rate_1 = db.get_result(f'SELECT buy_rate, sale_rate FROM currency WHERE bank = "{user_bank}" and date_exchange = "{user_date}" and currency = "{user_currency_1}"')
            buy_rate_2, sale_rate_2 = db.get_result(f'SELECT buy_rate, sale_rate FROM currency WHERE bank = "{user_bank}" and date_exchange = "{user_date}" and currency = "{user_currency_2}"')
        cur_exchange_buy = buy_rate_2 / buy_rate_1
        cur_exchange_sale = sale_rate_2 / sale_rate_1

        return render_template('data_form.html', cur_exchange_buy = cur_exchange_buy, cur_exchange_sale = cur_exchange_sale, user_currency_1 = user_currency_1, user_currency_2 = user_currency_2)
    else:
        return render_template('data_form.html')

if __name__ == "__main__":
    app.run()