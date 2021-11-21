from flask_login import UserMixin
from flask_restplus import fields

from app.dao import db, login_manager, ma, api


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)

    def __init__(self, login, password):
        self.login = login
        self.password = password


# for Swagger
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'login', 'password')


# dop param for decorator  @api.expect('model')
model = api.model('Resource', {
    'login': fields.String('Enter login'),
    'password': fields.String('Enter password')
})

user_schema = UserSchema()
users_schema = UserSchema(many=True)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
