from .db import db

class Umessage(db.Model):
    messageID = db.Column(db.Integer, primary_key = True)
    messageContent = db.Column(db.String(225))
    createDate = db.Column(db.Date())
    fromUserID = db.Column(db.Integer, db.ForeignKey('userdb.studentID'))
    toUserID = db.Column(db.Integer, db.ForeignKey('userdb.studentID'))
