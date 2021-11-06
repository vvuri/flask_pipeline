import os

# fix error  'cached_property' from 'werkzeug'
import werkzeug
from flask.scaffold import _endpoint_from_view_func
from werkzeug.utils import cached_property
import flask
flask.helpers._endpoint_from_view_func = _endpoint_from_view_func
werkzeug.cached_property = cached_property

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_restplus import Api


PSQL_CONNECTION = os.environ.get('PSQL_CONNECTION', '')

app = Flask(__name__)
CORS(app)
app.secret_key = 'hidden secret key'
# 'postgresql+psycopg2://user:password@ip_adress:5432/db_name' - real name in system environment PSQL_CONNECTION
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://' + PSQL_CONNECTION
# app.config['SQLALCHEMY_BINDS'] = {'schema': 'test_flask'}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
login_manager = LoginManager(app)
db = SQLAlchemy(app)

# for Swagger
ma = Marshmallow(app)
api = Api(doc='/swagger/')
api.init_app(app)


# сразу создать таблицы при запуске - не для продакшена
def create_database():
    db.create_all()
    db.session.commit()


from app.dao import models, routes
