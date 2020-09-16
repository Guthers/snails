from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger
from api.route import api_register
from argparse import ArgumentParser

def create_app():
    app = Flask(__name__)

    app.config['SWAGGER'] = {
        'title': 'Snail API Documentation',
        'description': 'A fantastic description of what the floop snails do'
    }
    swagger = Swagger(app)

    app.register_blueprint(api_register, url_prefix='/api')

    #app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://username:password@localhost/db_name"
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.db"

    # this is to shut up a warning and is PROBABLY fine
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    return app


app = create_app()
db = SQLAlchemy(app)

class User(db.Model):
    studentID = db.Column(db.Integer, primary_key = True)
    studentname = db.Column(db.String(225))
    bio = db.Column(db.String(225))
    createDate = db.Column(db.String(225)) # This was what was in DBschema.sql
    eposts = db.relationship('Epost', backref='author', lazy=True)
    messagesSent = db.relationship('Umessage', backref='fromUser', lazy=True)
    messagesRecv = db.relationship('Umessage', backref='toUser', lazy=True)
    likes = db.relationship("Liked", backref="user", lazy=True)

class Epost(db.Model):
    postID = db.Column(db.Integer, primary_key = True)
    authorID = db.Column(db.Integer, db.ForeignKey('user.studentID'), nullable=False)
    content = db.Column(db.String(225))
    createDate = db.Column(db.Date())
    likeCount = db.Column(db.Integer)
    likes = db.relationship("Liked", backref="epost", lazy=True)

class Umessage(db.Model):
    messageID = db.Column(db.Integer, primary_key = True)
    messageContent = db.Column(db.String(225))
    createDate = db.Column(db.Date())
    fromUserID = db.Column(db.Integer, db.ForeignKey('user.studentID'))
    toUserID = db.Column(db.Integer, db.ForeignKey('user.studentID'))

class Reply(db.Model):
    replyID = db.Column(db.Integer, primary_key = True)
    postID = db.Column(db.Integer, db.ForeignKey('epost.postID'))
    userID = db.Column(db.Integer, db.ForeignKey('user.studentID'))
    createDate = db.Column(db.Date())
    RepliedToName = db.Column(db.String(225))

class Liked(db.Model):
    __table_args__ = (
            db.PrimaryKeyConstraint('postID', 'userID'),
            )
    postID = db.Column(db.Integer, db.ForeignKey('epost.postID'))
    userID = db.Column(db.Integer, db.ForeignKey('user.studentID'))
    createDate = db.Column(db.Date())

class Board(db.Model):
    boardID = db.Column(db.Integer, primary_key = True)
    longitude = db.Column(db.Numeric)
    latitude = db.Column(db.Numeric)

db.create_all()

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port
    app.run(host='0.0.0.0', port=port)
