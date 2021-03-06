from .db import db
import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    username = db.Column(db.Text(32))
    password = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    entries = db.relationship('Entry', backref='author', lazy=True)
    messages_sent = db.relationship('Message',
            foreign_keys='Message.from_user_id', backref='from_user', lazy='dynamic')
    messages_recv = db.relationship('Message',
            foreign_keys='Message.to_user_id', backref='to_user', lazy='dynamic')
    likes = db.relationship("Liked", backref="user", lazy=True)

    @property
    def rolenames(self):
        return []

    @classmethod
    def lookup(cls, username):
        return cls.query.filter_by(username=username).one_or_none()

    @classmethod
    def identify(cls, id):
        return cls.query.get(id)

    @property
    def identity(self):
        return self.id