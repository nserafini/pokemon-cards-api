from flask import Flask

from api.config import Config
from api.controllers.card import (
    SingleCardController,
    SingleCardIDController
)
from api.utils.api import (
    BaseAPI,
    swagger_config
)
from api.utils.db import init_db


def create_app(config):
    """Initialize api db."""

    app = Flask(__name__)
    app.config.from_object(config)
    swagger_config(app)

    init_db(app)

    @app.route('/')
    def index():
        return "It works!"

    api = BaseAPI(app)
    api.add_resource(SingleCardController, '/cards')
    api.add_resource(SingleCardIDController, '/cards/<card_id>')

    return app


if __name__ == '__main__':
    app = create_app(Config())
    app.run(host="0.0.0.0", debug=True)
