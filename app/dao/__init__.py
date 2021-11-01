import os

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

PSQL_CONNECTION = os.environ.get('PSQL_CONNECTION', '')

app = Flask(__name__)
app.secret_key = 'hidden secret key'
# 'postgresql+psycopg2://user:password@ip_adress:5432/db_name' - real name in system environment PSQL_CONNECTION
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://'+PSQL_CONNECTION
# app.config['SQLALCHEMY_BINDS'] = {'schema': 'test_flask'}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
login_manager = LoginManager(app)
db = SQLAlchemy(app)


from app.dao import models, routes


# сразу создать таблицы при запуске - не для продакшена
def create_database():
    db.create_all()
    db.session.commit()
