from marshmallow import Schema, fields


class DNAKitOrderSchema(Schema):
    sequencing_type = fields.Str()
    user = fields.Str()
    shipping_info = fields.Str()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()

class UserSchema(Schema):
    email = fields.Email()
    name = fields.Str()
    created_at = fields.DateTime()
    orders = fields.Nested(DNAKitOrderSchema, many=True)
    phone_number = fields.Str()
