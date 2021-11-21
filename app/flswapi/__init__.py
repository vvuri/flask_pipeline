from flask import Flask
from flask_login import LoginManager
from flask_marshmallow import Marshmallow
from flask_restplus import Api


app = Flask(__name__)
app.secret_key = 'hidden secret key'
login_manager = LoginManager(app)

# for Swagger
ma = Marshmallow(app)
api = Api(
    doc='/swagger/',
    title='API Flask pipeline project',
    default='methods',
    default_label=''
)
api.init_app(app)


from app.flswapi import models, routes