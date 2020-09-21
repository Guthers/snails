from .db import db

class Liked(db.Model):
    __table_args__ = (
            db.PrimaryKeyConstraint('postID', 'userID'),
            )
    postID = db.Column(db.Integer, db.ForeignKey('epost.postID'))
    userID = db.Column(db.Integer, db.ForeignKey('userdb.studentID'))
    createDate = db.Column(db.Date())
