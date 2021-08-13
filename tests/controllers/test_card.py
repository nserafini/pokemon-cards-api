from unittest.mock import patch

from api.exceptions import NotFoundError
from api.models.enums import (
    CardExpansion,
    CardRarity,
    CardType
)
from api.utils.testing import DBTest


class TestCardController(DBTest):
    def setUp(self):
        self.create_card_payload = {
            "name": "Charizard",
            "hp": 100,
            "first_edition": True,
            "expansion": "Base Set",
            "type": "Fire",
            "rarity": "Common",
            "price": 100,
            "image_filename": "charizard.jpg"
        }
        self.mocked_create_card_service_response = {
            "hp": 100,
            "name": "charizard",
            "image_filename": "charizard.jpg",
            "id": "fc72c6ba-ef95-47f1-a835-7bbf8b462ab5",
            "price": 100,
            "expansion": CardExpansion.BASE_SET,
            "creation_date": "2021-08-13 02:37:26",
            "rarity": CardRarity.COMMON,
            "type": CardType.FIRE,
            "first_edition": True
        }
        self.expected_create_response = {
            'creation_date': '2021-08-13 02:37:26',
            'expansion': 'Base Set',
            'first_edition': True,
            'hp': 100,
            'id': 'fc72c6ba-ef95-47f1-a835-7bbf8b462ab5',
            'image_filename': 'charizard.jpg',
            'name': 'charizard',
            'price': 100,
            'rarity': 'Common',
            'type': 'Fire'
        }

    @patch("api.controllers.card.CardService.get_many")
    def test_get_all_cards_success(self, mocked_get_many):
        mocked_get_many.return_value = {
            'cards': [self.mocked_create_card_service_response]
        }
        response = self.test_client.get('/cards')
        assert response.json == {'cards': [self.expected_create_response]}

    @patch("api.controllers.card.CardService.get_many")
    def test_get_all_cards_error_not_found(self, mocked_get_many):
        mocked_get_many_response = {'cards': []}
        mocked_get_many.return_value = mocked_get_many_response
        response = self.test_client.get('/cards')
        assert response.json == mocked_get_many_response

    @patch("api.controllers.card.CardService.create")
    def test_create_card_success(self, mocked_create):
        mocked_create.return_value = self.mocked_create_card_service_response
        response = self.test_client.post(
            '/cards',
            json=self.create_card_payload
        )
        assert response.json == self.expected_create_response

    @patch("api.controllers.card.CardService.get_one")
    def test_get_one_card_success(self, mocked_get_one):
        mocked_get_one.return_value = self.mocked_create_card_service_response
        response = self.test_client.get(
            f"/cards/{self.mocked_create_card_service_response['id']}"
        )
        assert response.json == self.expected_create_response

    @patch("api.controllers.card.CardService.get_one")
    def test_get_one_card_not_found(self, mocked_get_one):
        random_uuid = "93fb3b57-1895-4f7b-ab8a-6853de44f606"
        mocked_get_one.side_effect = NotFoundError(f"{random_uuid} not found")
        response = self.test_client.get(f"/cards/{random_uuid}")
        assert response.json == {"error": f"{random_uuid} not found"}
        assert response.status_code == 404

    @patch("api.controllers.card.CardService.delete")
    def test_delete_card_success(self, mocked_delete):
        random_uuid = "93fb3b57-1895-4f7b-ab8a-6853de44f606"
        mocked_delete.side_effect = None
        response = self.test_client.delete(f"/cards/{random_uuid}")
        assert response.status_code == 204

    @patch("api.controllers.card.CardService.delete")
    def test_delete_card_not_found(self, mocked_delete):
        random_uuid = "93fb3b57-1895-4f7b-ab8a-6853de44f606"
        mocked_delete.side_effect = NotFoundError(f"{random_uuid} not found")
        response = self.test_client.delete(f"/cards/{random_uuid}")
        assert response.json == {"error": f"{random_uuid} not found"}
        assert response.status_code == 404
