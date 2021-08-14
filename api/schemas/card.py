from marshmallow import (
    Schema,
    fields,
    post_load
)
from marshmallow.validate import Range

from marshmallow_enum import EnumField

from api.models.enums import (
    CardExpansion,
    CardRarity,
    CardType
)


class CardGetOneResponseSchema(Schema):
    """Schema to get one card response."""

    id = fields.Str()
    name = fields.Str()
    hp = fields.Integer()
    first_edition = fields.Boolean()
    expansion = EnumField(CardExpansion, dump_by=EnumField.VALUE)
    type = EnumField(CardType, dump_by=EnumField.VALUE)
    rarity = EnumField(CardRarity, dump_by=EnumField.VALUE)
    price = fields.Integer()
    image_filename = fields.Str()
    creation_date = fields.Str()


class CardGetAllResponseSchema(Schema):
    """Schema to get all cards response."""

    cards = fields.Nested(CardGetOneResponseSchema, many=True)
    page_number = fields.Integer()
    page_size = fields.Integer()
    total_items = fields.Integer()


class CardGetAllRequestSchema(Schema):
    """Schema to get all cards request."""

    name = fields.Str()
    hp = fields.Integer()
    first_edition = fields.Boolean()
    expansion = fields.Str()
    type = fields.Str()
    rarity = fields.Str()
    price = fields.Integer()
    image_filename = fields.Str()
    page = fields.Integer()


class CardCreateRequestSchema(Schema):
    """Schema to create card request."""

    name = fields.Str(required=True)
    hp = fields.Integer(required=True, validate=[
        Range(min=0, error="min value: 0"),
        Range(max=100, error="max value: 100")
    ])
    first_edition = fields.Boolean(required=True)
    expansion = EnumField(
        CardExpansion, load_by=EnumField.VALUE, required=True)
    type = EnumField(CardType, load_by=EnumField.VALUE, required=True)
    rarity = EnumField(CardRarity, load_by=EnumField.VALUE, required=True)
    price = fields.Integer(required=True, validate=[
        Range(min=0, error="min value: 0"),
        Range(max=1000, error="max value: 1000")
    ])
    image_filename = fields.Str(required=True)

    @post_load
    def validate_hp(self, data, **args):
        hp = data.get('hp')
        if hp and hp % 10 != 0:
            raise ValueError("HP must be a multiple of 10")
        return data


class CardUpdateRequestSchema(Schema):
    """Schema to update card request."""

    name = fields.Str()
    hp = fields.Integer(validate=[
        Range(min=0, error="min value: 0"),
        Range(max=100, error="max value: 100")
    ])
    first_edition = fields.Boolean()
    expansion = EnumField(CardExpansion, load_by=EnumField.VALUE)
    type = EnumField(CardType, load_by=EnumField.VALUE)
    rarity = EnumField(CardRarity, load_by=EnumField.VALUE)
    price = fields.Integer(validate=[
        Range(min=0, error="min value: 0"),
        Range(max=1000, error="max value: 1000")
    ])
    image_filename = fields.Str()

    @post_load
    def validate_hp(self, data, **args):
        hp = data.get('hp')
        if hp and hp % 10 != 0:
            raise ValueError("HP must be a multiple of 10")
        return data
