import sqlite3
from flask_restful import Resource, reqparse
# from flask_jwt import jwt_required, current_identity
from models.user import UserModel

class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "A user with that username already exists"}, 400
        
        user = UserModel(**data)
        user.save_to_db()

        return {"message": "User created successfully."}, 201
