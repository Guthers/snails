from .db import db
import datetime

class User(db.Model):
    id = db.Column(db.String(255), primary_key = True)
    name = db.Column(db.String(255))
    bio = db.Column(db.String(255)) # pretty sure this doesn't work
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    entries = db.relationship('Entry', backref='author', lazy=True)
    messages_sent = db.relationship('Message',
            foreign_keys='Message.from_user_id', backref='from_user', lazy='dynamic')
    messages_recv = db.relationship('Message',
            foreign_keys='Message.to_user_id', backref='to_user', lazy='dynamic')
    likes = db.relationship("Liked", backref="user", lazy=True)
