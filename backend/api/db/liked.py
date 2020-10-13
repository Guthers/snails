from .db import db
import datetime

class Liked(db.Model):
    __table_args__ = (db.PrimaryKeyConstraint('entry_id', 'user_id'),)
    entry_id = db.Column(db.Integer, db.ForeignKey('entry.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
