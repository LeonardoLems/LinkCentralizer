from marshmallow import Schema, fields, validate

class UserSchema(Schema):
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True)
    last_name = fields.Str(required=True)
    city = fields.Str(required=True)
    country = fields.Str(required=True)
    state = fields.Str(required=True)


"""
 id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50))
    country = db.Column(db.String(40))
    state = db.Column(db.String(40))
"""