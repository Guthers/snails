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

db.create_all()

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port
    app.run(host='0.0.0.0', port=port)
