from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger
from argparse import ArgumentParser

DBM = "mysql+pymysql"
HST = "localhost"
DTB = "snails"
USR = "root"
PWD = "INSERT PASSWORD"
PRT = "3306"
CONNECTION_STRING = f"{DBM}://{USR}:{PWD}@{HST}:{PRT}/{DTB}"

def create_app():
    app = Flask(__name__)

    app.config['SWAGGER'] = {
        'title': 'Snail API Documentation',
        'description': 'A fantastic description of what the floop snails do'
    }
    swagger = Swagger(app)

    #app.config['SQLALCHEMY_DATABASE_URI'] = CONNECTION_STRING
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.db"

    # this is to shut up a warning and is PROBABLY fine
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    return app


# Create the inital app
app = create_app()

# Then register all the endpoints (which need the app base to be made)
from api.route import api_register
app.register_blueprint(api_register, url_prefix='/api')

# This should only be done once, and shouldn't be in the root, but will work for now
from api.db import db
db.drop_all()
db.create_all()


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port
    app.run(host='0.0.0.0', port=port)
