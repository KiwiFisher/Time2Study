from marshmallow import Schema
from marshmallow import fields

from models import Reel, Line


class ReelSchema(Schema):
    class Meta(Schema):
        model = Reel
        exclude = ('updated_at', 'created_at', 'mono_id', 'mono_line', 'braid_id', 'braid_line')

    id = fields.Int()
    brand = fields.Str()
    model = fields.Str()


class LineSchema(Schema):
    class Meta(Schema):
        model = Line
        exclude = ('updated_at', 'created_at')

    brand = fields.Str()
    model = fields.Str()
    strength = fields.Str()
    diameter = fields.Float()
    packing = fields.Float()
