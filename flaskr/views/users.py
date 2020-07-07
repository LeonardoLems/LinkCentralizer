from flask_restful import Resource

class UserView(Resource):
    def get(self):
        return "hellow world"