from .db import db

class Epost(db.Model):
    postID = db.Column(db.Integer, primary_key = True)
    authorID = db.Column(db.Integer, db.ForeignKey('userdb.studentID'), nullable=False)
    content = db.Column(db.String(255))
    createDate = db.Column(db.Date())
    likeCount = db.Column(db.Integer)
    likes = db.relationship("Liked", backref="epost", lazy=True)