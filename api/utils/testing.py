import unittest

from app import create_app

from api.db import db

db.session.session_factory.configure(expire_on_commit=False)


class BaseTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = create_app()
        cls.test_client = cls.app.test_client()
        ctx = cls.app.app_context()
        ctx.push()


class DBTest(BaseTest):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.db = db

    @classmethod
    def tearDown(cls):
        cls.db.session.rollback()
        cls.db.session.remove()
        cls.db.drop_all()
        cls.db.create_all()

    def save(self, model, payload):
        model = model(**payload)
        self.db.session.add(model)
        self.db.session.commit()
        return model
