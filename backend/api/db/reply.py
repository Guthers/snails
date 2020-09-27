from .db import db

class Reply(db.Model):
    replyID = db.Column(db.Integer, primary_key = True)
    postID = db.Column(db.Integer, db.ForeignKey('epost.postID'))
    userID = db.Column(db.String(255), db.ForeignKey('userdb.studentID'))
    createDate = db.Column(db.Date())
    RepliedToName = db.Column(db.String(255))
