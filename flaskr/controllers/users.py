from models.users import User
from werkzeug.security import generate_password_hash

class UserController:
    @staticmethod
    def register_user(data):
        # password = generate_password_hash(data.pop("password"))
        password = data.pop("password")
        return User.create_user(data, password)
