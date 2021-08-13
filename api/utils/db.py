from api.db import db


def init_db(app):
    """Initialize api db."""

    with app.app_context():
        db.init_app(app)
        db.create_all()
