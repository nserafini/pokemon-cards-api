from flask import request

from flask_restful import Resource

from api.schemas.card import (
    CardCreateRequestSchema,
    CardGetAllRequestSchema,
    CardGetAllResponseSchema,
    CardGetOneResponseSchema,
    CardUpdateRequestSchema
)
from api.services.card import CardService
from api.utils.api import validate_access


class SingleCardController(Resource):
    """Exposes get and create REST methods."""

    @validate_access
    def get(self):
        """Retrieve many cards by filters."""

        filters = request.args.to_dict()
        CardGetAllRequestSchema().load(filters)
        cards = CardService.get_many(filters)
        return CardGetAllResponseSchema().dump(cards), 200

    @validate_access
    def post(self):
        """Create a card."""

        payload = request.get_json()
        CardCreateRequestSchema().load(payload)
        card = CardService.create(payload)
        return CardGetOneResponseSchema().dump(card), 201


class SingleCardIDController(Resource):
    """Exposes get, update and delete REST methods."""

    @validate_access
    def get(self, card_id):
        """Retrieve a card by id."""

        card = CardService.get_one(card_id)
        return CardGetOneResponseSchema().dump(card), 200

    @validate_access
    def patch(self, card_id):
        """Update a card by id."""

        payload = request.get_json()
        CardUpdateRequestSchema().load(payload)
        card = CardService.update(card_id, payload)
        return CardGetOneResponseSchema().dump(card), 200

    @validate_access
    def delete(self, card_id):
        """Delete a card by id."""

        CardService.delete(card_id)
        return None, 204
