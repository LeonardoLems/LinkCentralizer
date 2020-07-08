from flask_restful import Resource


class CatalogView(Resource):
    def get(self):
        return "catalog Ok"
