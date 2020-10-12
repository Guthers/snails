from .db import db
import datetime

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String(255))
    author_id = db.Column(db.String(255), db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    reply_id = db.Column(db.Integer, db.ForeignKey('entry.id'))
    likes = db.relationship("Liked", backref="entry", lazy=True)
    replies = db.relationship("Entry", 
                              cascade="all,delete",
                              backref=db.backref("parent", remote_side=[id]), 
                              lazy='dynamic')
