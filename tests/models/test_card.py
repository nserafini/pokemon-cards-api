import pytest

from marshmallow import ValidationError
from sqlalchemy.exc import DataError

from api.models.card import CardModel
from api.utils.testing import DBTest

class TestCardModel(DBTest):

    def setUp(self):

        self.card_payload = {
            "name": "Charizard",
            "hp": 100,
            "first_edition": True,
            "expansion": "BASE_SET",
            "type": "FIRE",
            "rarity": "COMMON",
            "price": 500,
            "image_filename": "charizard.jpg"
        }

    def test_create_card_success(self):
        self.save(CardModel, self.card_payload)

    def test_create_card_hp_multiple_10_validation_error(self):
        payload = self.card_payload.copy()
        payload['hp'] = 15
        with pytest.raises(ValidationError):
            self.save(CardModel, payload)

    def test_create_card_expansion_error(self):
        payload = self.card_payload.copy()
        payload['expansion'] = "foo"
        with pytest.raises(DataError):
            self.save(CardModel, payload)
        
    def test_create_card_type_error(self):
        payload = self.card_payload.copy()
        payload['type'] = "foo"
        with pytest.raises(DataError):
            self.save(CardModel, payload)

    def test_create_card_rarity_error(self):
        payload = self.card_payload.copy()
        payload['rarity'] = "foo"
        with pytest.raises(DataError):
            self.save(CardModel, payload)