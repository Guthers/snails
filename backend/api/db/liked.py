from .db import db

class Liked(db.Model):
    __table_args__ = (
            db.PrimaryKeyConstraint('post_id', 'user_id'),
            )
    post_id = db.Column(db.Integer, db.ForeignKey('epost.post_id'))
    user_id = db.Column(db.String(255), db.ForeignKey('userdb.student_id'))
    create_date = db.Column(db.Date())
