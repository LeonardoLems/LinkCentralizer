from . import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50))
    country = db.Column(db.String(40))
    state = db.Column(db.String(40))
    catalog = db.relationship('Catalog', backref='user', lazy=True)

