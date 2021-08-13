import pytest

from sqlalchemy.exc import (
    IntegrityError,
    InvalidRequestError
)

from api.exceptions import NotFoundError
from api.services.card import CardService
from api.utils.testing import DBTest


class TestCardService(DBTest):
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
        card = CardService.create(self.card_payload)
        assert card

    def test_create_card_error_missing_fields(self):
        with pytest.raises(IntegrityError):
            CardService.create({})

    def test_update_card_success(self):
        card = CardService.create(self.card_payload)
        new_hp = 50
        card = CardService.update(card.id, {"hp": new_hp})
        assert card.hp == new_hp

    def test_update_card_error_unkown_value(self):
        card = CardService.create(self.card_payload)
        with pytest.raises(InvalidRequestError):
            CardService.update(card.id, {"foo": "foo"})

    def test_get_one_card_success(self):
        card = CardService.create(self.card_payload)
        card = CardService.get_one(card.id)
        assert card.id

    def test_get_one_card_error_not_found(self):
        random_uuid = "93fb3b57-1895-4f7b-ab8a-6853de44f606"
        with pytest.raises(NotFoundError):
            CardService.get_one(random_uuid)

    def test_get_many_cards_success(self):
        payload_one = self.card_payload.copy()
        CardService.create(payload_one)

        payload_two = self.card_payload.copy()
        payload_two["name"] = "test"
        CardService.create(payload_two)

        filters = {"type": "FIRE"}
        response = CardService.get_many(filters)
        assert len(response['cards']) == 2

    def test_get_many_cards_error_not_found(self):
        filters = {"type": "FIRE"}
        response = CardService.get_many(filters)
        assert len(response['cards']) == 0

    def test_delete_card_success(self):
        card = CardService.create(self.card_payload)
        CardService.delete(card.id)
        with pytest.raises(NotFoundError):
            CardService.get_one(card.id)

    def test_delete_card_error_not_found(self):
        random_uuid = "93fb3b57-1895-4f7b-ab8a-6853de44f606"
        with pytest.raises(NotFoundError):
            CardService.delete(random_uuid)
