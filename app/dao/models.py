from flask_login import UserMixin
from flask_restplus import fields

from app.dao import db, login_manager, ma, api


class Message(db.Model):
    # __table_args__ = {'schema': 'test_flask'}

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(1024), nullable=False)

    def __init__(self, text, tags):
        self.text = text.strip()
        self.tags = [
            Tag(text=tag.strip()) for tag in tags.split(',')
        ]


# for Swagger
class MessageSchema(ma.Schema):
    class Meta:
        fields = ('id', 'text')


message_schema = MessageSchema()
messages_schema = MessageSchema(many=True)


class Tag(db.Model):
    # __table_args__ = {'schema': 'test_flask'}

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(64), nullable=False)

    message_id = db.Column(db.Integer, db.ForeignKey('message.id'), nullable=False)
    message = db.relationship('Message', backref=db.backref('tags', lazy=True))


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
model = api.model(model={
    'login': fields.String('Enter login'),
    'password': fields.String('Enter password')
})

user_schema = UserSchema()
users_schema = UserSchema(many=True)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
