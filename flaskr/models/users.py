from . import db
from typing import Dict, Tuple


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50))
    country = db.Column(db.String(40))
    state = db.Column(db.String(40))
    catalog = db.relationship('Catalog', backref='user', lazy=True)

    @classmethod
    def create_user(cls, data: Dict, password: str) -> Tuple:
        try:
            user: User = cls(password=password, **data)
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            return 500, e
        return user, 201

    @classmethod
    def delete_user(cls, id):
        pass

    @classmethod
    def edit_user(cls, id, data):
        pass
