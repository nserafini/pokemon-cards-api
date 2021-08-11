from flask import Flask

from api.config import Config
from api.db import db


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())

    db.init_app(app)

    @app.route('/')
    def index():
        return "It works!"

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host="0.0.0.0", debug=True)
