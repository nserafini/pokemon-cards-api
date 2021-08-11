import unittest

from app import create_app

from api.db import db

db.session.session_factory.configure(expire_on_commit=False)


class BaseTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = create_app()
        cls.test_client = cls.app.test_client()


class DBTest(BaseTest):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.db = db
        with cls.app.app_context():
            cls.db.drop_all()
            cls.db.create_all()

    def save(self, model, payload):
        with self.app.app_context():
            model = model(**payload)
            self.db.session.add(model)
            self.db.session.commit()
        return model
