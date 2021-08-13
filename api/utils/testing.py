import unittest

from app import create_app

from flask import testing

from werkzeug.datastructures import Headers

from api.config import TestConfig
from api.db import db

db.session.session_factory.configure(expire_on_commit=False)


class TestAuthenticatedClient(testing.FlaskClient):
    def open(self, *args, **kwargs):
        api_key_headers = Headers({
            'Api-Key': 'secret'
        })
        headers = kwargs.pop('headers', Headers())
        headers.extend(api_key_headers)
        kwargs['headers'] = headers
        return super().open(*args, **kwargs)


class BaseTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = create_app(TestConfig())
        cls.app.test_client_class = TestAuthenticatedClient
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
