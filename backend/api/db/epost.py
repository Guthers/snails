from .db import db
import datetime

class Epost(db.Model):
    __tablename__ = "epost"
    post_id = db.Column(db.Integer, primary_key = True)
    reply_id = db.Column(db.Integer, db.ForeignKey('epost.post_id'))
    author_id = db.Column(db.String(255), db.ForeignKey('userdb.student_id'), nullable=False)
    content = db.Column(db.String(255))
    create_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    likes = db.relationship("Liked", backref="epost", lazy=True)
    replies = db.relationship("Epost", cascade="all,delete",
            backref=db.backref("parent", remote_side=[post_id]), lazy=True)
