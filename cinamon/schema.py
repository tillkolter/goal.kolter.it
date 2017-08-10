from marshmallow import Schema, fields


class SynonymSchema(Schema):
    id = fields.Int()
    meaning = fields.Str(required=True)
    words = fields.List(fields.String)
