from app.dao import db


class Message(db.Model):
    # __table_args__ = {'schema': 'test_flask'}

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(1024), nullable=False)

    def __init__(self, text, tags):
        self.text = text.strip()
        self.tags = [
            Tag(text=tag.strip()) for tag in tags.split(',')
        ]


class Tag(db.Model):
    # __table_args__ = {'schema': 'test_flask'}

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(64), nullable=False)

    message_id = db.Column(db.Integer, db.ForeignKey('message.id'), nullable=False)
    message = db.relationship('Message', backref=db.backref('tags', lazy=True))
