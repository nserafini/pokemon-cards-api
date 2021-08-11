from marshmallow import ValidationError

from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Enum
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import validates

from api.models.base import BaseModel
from api.models.enums import CardExpansion
from api.models.enums import CardRarity
from api.models.enums import CardType


class CardModel(BaseModel):

    __tablename__ = "cards"

    name = Column(String(128), nullable=False)
    hp = Column(Integer, nullable=False)
    first_edition = Column(Boolean, nullable=False)
    expansion = Column(Enum(CardExpansion), nullable=False)
    type = Column(Enum(CardType), nullable=False)
    rarity = Column(Enum(CardRarity), nullable=False)
    price = Column(Integer, nullable=False)
    image_filename = Column(String(128), nullable=False)

    @validates('hp')
    def validate_name(self, key, value):
        if value % 10 != 0:
            raise ValidationError("HP must be a multiple of 10")
        return value
