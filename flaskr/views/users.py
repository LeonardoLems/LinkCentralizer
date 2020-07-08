from flask_restful import Resource, reqparse, request
from schemas.user import UserSchema
from controllers.users import UserController
from marshmallow import ValidationError

class UserView(Resource):
    def get(self):
        return "hellow world"

    def post(self):
        post_data = request.get_json()
        user_schema = UserSchema()
        try:
            data = user_schema.load(post_data)
        except ValidationError as err:
            return err.messages

        user, status_code = UserController.register_user(data)
        user_data = user_schema.dump(user).remove("password")
        if status_code == 201:
            return status_code, user_data
