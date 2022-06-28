from marshmallow import Schema, fields


class UserSchema(Schema):
    email = fields.Email()
    name = fields.Str()
    created_at = fields.DateTime()
