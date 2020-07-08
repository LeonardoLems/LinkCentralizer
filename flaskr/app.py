import os
from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate

from views.users import UserView
from views.catalog import CatalogView

from models import db
from config import config
from models.users import User
from models.catalog import Catalog, Item, Page


def create_api(app: Flask) -> None:
    """
    function that creates api
    :param app:
    :return:
    """
    api: Api = Api(app)
    api.add_resource(UserView, '/api/v1/user/')
    api.add_resource(CatalogView, '/api/v1/catalog/')
    # api.add_resource(UserView, '/')


def create_app() -> Flask:
    """
    function that creates api
    :return: app
    """
    app: Flask = Flask(__name__, instance_relative_config=True)
    flask_env: str = os.getenv("FLASK_ENV")

    app.config.from_object(config[flask_env])

    db.init_app(app)
    create_api(app)
    migrate = Migrate(app, db)

    return app
