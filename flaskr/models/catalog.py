from . import db
from .users import User


class Catalog(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    item = db.relationship('Item', backref='catalog', lazy=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    page_style_id = db.Column(db.Integer, db.ForeignKey('page.id'),
                              nullable=False)


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    icon_url = db.Column(db.String(200), nullable=True)
    url = db.Column(db.String(200), nullable=True)
    color = db.Column(db.String(10), nullable=True)
    catalog_id = db.Column(db.Integer, db.ForeignKey('catalog.id'),
                           nullable=False)


class Page(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    catalog = db.relationship('Catalog', backref='page', lazy=True)
    font = db.Column(db.String(30), nullable=True)
    img_background = db.Column(db.String(200), nullable=True)
    bg_color = db.Column(db.String(10), nullable=True)

