from marshmallow import (
    Schema,
    fields,
    post_load
)

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


class CardCreateRequestSchema(Schema):
    """Schema to create card request."""

    name = fields.Str(required=True)
    hp = fields.Integer(required=True)
    first_edition = fields.Boolean(required=True)
    expansion = EnumField(
        CardExpansion, load_by=EnumField.VALUE, required=True)
    type = EnumField(CardType, load_by=EnumField.VALUE, required=True)
    rarity = EnumField(CardRarity, load_by=EnumField.VALUE, required=True)
    price = fields.Integer(required=True)
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
    hp = fields.Integer()
    first_edition = fields.Boolean()
    expansion = EnumField(CardExpansion, load_by=EnumField.VALUE)
    type = EnumField(CardType, load_by=EnumField.VALUE)
    rarity = EnumField(CardRarity, load_by=EnumField.VALUE)
    price = fields.Integer()
    image_filename = fields.Str()

    @post_load
    def validate_hp(self, data, **args):
        hp = data.get('hp')
        if hp and hp % 10 != 0:
            raise ValueError("HP must be a multiple of 10")
        return data
