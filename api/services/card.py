from api.db import db
from api.exceptions import NotFoundError
from api.models.card import CardModel


class CardService:
    """Manage card model."""

    _model = CardModel

    @classmethod
    def create(cls, card_payload):
        """Creates card."""

        model = cls._model(**card_payload)
        db.session.add(model)
        db.session.commit()
        return model

    @classmethod
    def update(cls, card_id, card_payload):
        """Updates a card."""

        db.session.query(cls._model).filter_by(id=card_id).update(card_payload)
        db.session.commit()
        card = cls.get_one(card_id)
        return card

    @classmethod
    def get_one(cls, card_id):
        """Retrieves a card by filters."""

        card = cls._model.query.get(card_id)
        if not card:
            raise NotFoundError(f"{card_id} not found")
        return card

    @classmethod
    def get_many(cls, filters):
        """Retrieves many cards by filters."""

        cards = cls._model.query.filter_by(**filters).all()
        return {"cards": cards}

    @classmethod
    def delete(cls, card_id):
        """Deletes a card."""

        card = cls.get_one(card_id)
        db.session.delete(card)
        db.session.commit()
