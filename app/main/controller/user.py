from flask import request
from flask_restx import Resource

from app.main.util.user import UserDTO
from app.main.repository.user import UserRepository

api = UserDTO.api
user_repo = UserRepository()


@api.route("")
class Users(Resource):
    @api.doc("list of registered users")
    @api.marshal_list_with(UserDTO.user, envelope="data")
    def get(self):
        return user_repo.get_all_users(), 200

    @api.response(201, description="user successfully created")
    @api.doc("create new user")
    @api.expect(UserDTO.user_request, validate=True)
    def post(self):
        data = request.json
        return user_repo.create_user(data=data), 201


@api.route("/<id>")
class UserById(Resource):
    @api.response(200, description="user detail successfully featch")
    @api.doc("detail of registered users")
    @api.marshal_with(UserDTO.user, envelope="data")
    def get(self, id: int):
        return user_repo.get_user_by_id(id), 200

    @api.response(204, description="user successfully deleted")
    @api.doc("delete registered user")
    def delete(self, id: int):
        return user_repo.delete_user_by_id(id), 204
