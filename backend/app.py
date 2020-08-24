from flask import Flask
from flasgger import Swagger
from api.route.home import home_api
from argparse import ArgumentParser


def create_app():
    app = Flask(__name__)

    app.config['SWAGGER'] = {
        'title': 'Flask API Starter Kit',
    }
    swagger = Swagger(app)

    app.register_blueprint(home_api, url_prefix='/api')

    return app


app = create_app()
if __name__ == '__main__':
    app.run(host='0.0.0.0')
