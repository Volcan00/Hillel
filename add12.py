from flask import Flask, render_template, request
from db_manager import *
from celery_working import *
import al_db
import models_db
from sqlalchemy import select
from sqlalchemy.orm import Session
from flask import session as flask_session
from flask_session import Session as FlaskSession

app = Flask(__name__)
app.secret_key = "supersecret"

@app.route("/", methods = ['GET', 'POST'])
def login_user():
    if request.method == 'POST':
        with Session(al_db.engine) as session:
            query = select(models_db.User).filter(models_db.User.username == request.form["usernamelogin"])
            result = session.execute(query).fetchall()
            if result:
                flask_session["username"] = request.form["username"]
            else:
                return render_template("index.html", username = "No user found")
            return render_template("index.html", username = flask_session["username"])
    else: 
        return render_template("login.html")

@app.route("/logout", methods = ['GET'])
def logout_user():
    flask_session.pop("username", None)
    return "<p>Logout</p>"


@app.route("/register", methods = ['GET', 'POST'])
def register_user():
        return "<p>Logout</p>"
    

@app.route("/user_page", methods = ['GET'])
def index():
    if "username" in flask_session:
        return f'Logged in as {flask_session["username"]}'
    return "You are not logged in"

@app.route("/currency", methods = ['GET', 'POST'])
def currency_convert():
    if request.method == 'POST':
        user_bank = request.form['bank']
        user_currency_1 = request.form['currency_1']
        user_date = request.form['date']
        user_currency_2 = request.form['currency_2']
    
        with Session(al_db.engine) as session:
            statement_1 = select(models_db.Currency).filter_by(bank = user_bank, currency = user_currency_1, date_exchange = user_date)
            currency_1 = session.scalars(statement_1).first()
            statement_2 = select(models_db.Currency).filter_by(bank = user_bank, currency = user_currency_2, date_exchange = user_date)
            currency_2 = session.scalars(statement_2).first()

        buy_rate_1, sale_rate_1 = currency_1.buy_rate, currency_1.sale_rate
        buy_rate_2, sale_rate_2 = currency_2.buy_rate, currency_2.sale_rate

        cur_exchange_buy = buy_rate_2 / buy_rate_1
        cur_exchange_sale = sale_rate_2 / sale_rate_1

        return render_template('data_form.html', 
                               cur_exchange_buy = cur_exchange_buy, 
                               cur_exchange_sale = cur_exchange_sale, 
                               user_currency_1 = user_currency_1, 
                               user_currency_2 = user_currency_2,
                               username = flask_session["username"])
    else:
        if "username" in flask_session:
            return render_template('data_form.html', username = flask_session["username"])
        else:
            return "LOGIN FIRST"
        
if __name__ == "__main__":
    app.run(host="0.0.0.0")