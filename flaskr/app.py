import os
from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate

from views.users import UserView

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
    api.add_resource(CatalogResource, '/api/v1/catalog/')
    api.add_resource(UserView, '/')


def create_app() -> Flask:
    """
    function that creates api
    :return: app
    """
    app = Flask(__name__, instance_relative_config=True)
    flask_env = os.getenv("FLASK_ENV")

    app.config.from_object(config[flask_env])

    db.init_app(app)
    create_api(app)
    migrate = Migrate(app, db)

    return app


# application = create_app()
# db = SQLAlchemy(application)
# migrate = Migrate(application, db)

# from models.catalog_model import Catalog

# if __name__ == "__main__":
#     app_run = create_app()
#     app_run.run(host='0.0.0.0', port=8000, debug=True)
