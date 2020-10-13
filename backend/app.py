import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger
from argparse import ArgumentParser

def create_app():
    app = Flask(__name__)

    app.config['SWAGGER'] = {
        'title': 'Snail API',
        'description': 'Endpoints for interacting the coolest snail backend.',
        'version': "0.3.0"
    }
    swagger = Swagger(app)

    if app.config['ENV'] == 'production':
        DBM = "mysql+pymysql"
        HST = "localhost"
        DTB = "snails"
        USR = "root"
        PWD = "19dc1ae749b63d14"
        PRT = "3306"
        CONNECTION_STRING = f"{DBM}://{USR}:{PWD}@{HST}:{PRT}/{DTB}"
    else:
        CONNECTION_STRING = "sqlite:///test.db"

    app.config['SQLALCHEMY_DATABASE_URI'] = CONNECTION_STRING

    # this is to shut up a warning and is PROBABLY fine
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.config['SECRET_KEY'] = 'top secret'
    app.config['JWT_ACCESS_LIFESPAN'] = {'hours': 24}
    app.config['JWT_REFRESH_LIFESPAN'] = {'days': 30}


    return app


# Create the inital app
app = create_app()

# Then register all the endpoints (which need the app base to be made)
from api.route import api_register
app.register_blueprint(api_register, url_prefix='/api')

@app.cli.command("populate")
def populate_db():
    from datetime import datetime
    from api.db import db, Entry, Message, User
    from api.guard import guard

    # Drop tables
    db.drop_all()

    # Create tables
    db.create_all()

    print("Creating test user hooty...")
    print("Creating test user amityblight...")
    print("Creating test user theowllady...")
    print("Creating test user itsgus...")
    pwd = str(input("Enter password for test users: "))

    # Create users
    user_hooty = User(username="hooty", password=guard.hash_password(pwd), name="Hooty", created_at=datetime.now())
    user_amity = User(username="amityblight", password=guard.hash_password(pwd), name="Amity Blight", created_at=datetime.now())
    user_eda = User(username="theowllady", password=guard.hash_password(pwd), name="Eda Clawthorne", created_at=datetime.now())
    user_gus = User(username="itsgus", password=guard.hash_password(pwd), name="Gus", created_at=datetime.now())

    db.session.add(user_hooty)
    db.session.add(user_amity)
    db.session.add(user_eda)
    db.session.add(user_gus)
    db.session.commit()

    # Create entries
    content_amity = ["Where can I get style guides and advice on presentation, referencing and citation?",
                     "What services does Academic Skills offer?",
                     "How should I reference my sources in assignments?"]
    content_eda = ["What do examiners look for in a PhD / Research Doctorate thesis?",
                   "Will I be able to collect a Student Diary?",
                   "Where can I find academic writing and study skills workshops and seminars?"]
    content_gus = ["How can I find Staff and Student contact details?",
                    "What is the word limit for a PhD thesis?",
                    "Best cafe @ UQ?"]
    for cs, u in [(content_amity, user_amity), (content_eda, user_eda), (content_gus, user_gus)]:
        for c in cs:
            row = Entry(reply_id=None, author_id=u.id, content=c, created_at=datetime.now())
            db.session.add(row)

    # Replies
    db.session.add(Entry(reply_id=9, author_id=user_hooty.id, content="Merlo", created_at=datetime.now()))
    db.session.add(Entry(reply_id=10, author_id=user_amity.id, content="Eww", created_at=datetime.now()))
    db.session.add(Entry(reply_id=11, author_id=user_hooty.id, content="no u. HOOT HOOT", created_at=datetime.now()))
    db.session.add(Entry(reply_id=9, author_id=user_gus.id, content="Nah wordies", created_at=datetime.now()))
    db.session.add(Entry(reply_id=9, author_id=user_eda.id, content="Bean.", created_at=datetime.now()))

    # Messages
    db.session.add(Message(content="HAI AMITY!!", from_user_id=user_hooty.id, to_user_id=user_amity.id, created_at=datetime.now()))
    db.session.add(Message(content="Ew. Don't talk to me bird tube.", from_user_id=user_amity.id, to_user_id=user_hooty.id, created_at=datetime.now()))
    db.session.add(Message(content="Aww that's the best nickname ever been given to me!", from_user_id=user_hooty.id, to_user_id=user_amity.id, created_at=datetime.now()))
    db.session.add(Message(content="Dont talk to me again...", from_user_id=user_amity.id, to_user_id=user_hooty.id, created_at=datetime.now()))
    db.session.add(Message(content="I mean it.", from_user_id=user_amity.id, to_user_id=user_hooty.id, created_at=datetime.now()))
    db.session.add(Message(content="Awww, I like you too!", from_user_id=user_hooty.id, to_user_id=user_amity.id, created_at=datetime.now()))
    db.session.add(Message(content="smh my head.", from_user_id=user_amity.id, to_user_id=user_hooty.id, created_at=datetime.now()))
    db.session.add(Message(content="Just let me talk to luz", from_user_id=user_amity.id, to_user_id=user_hooty.id, created_at=datetime.now()))
    db.session.add(Message(content="Heads up. Amity is in the house", from_user_id=user_hooty.id, to_user_id=user_eda.id, created_at=datetime.now()))
    db.session.add(Message(content="HOOT HOOT", from_user_id=user_hooty.id, to_user_id=user_eda.id, created_at=datetime.now()))
    db.session.add(Message(content="Go away hooty.", from_user_id=user_eda.id, to_user_id=user_hooty.id, created_at=datetime.now()))
    db.session.add(Message(content="Hey kid. Here to see luz? ;)", from_user_id=user_eda.id, to_user_id=user_amity.id, created_at=datetime.now()))

    db.session.commit()

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port
    app.run(host='0.0.0.0', port=port)
