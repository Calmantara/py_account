from flask_restx import Namespace, fields


class UserDTO:
    api = Namespace("user", description="user related operations dto")
    user = api.model(
        "user",
        model={
            "id": fields.Integer(required=True, description="user id"),
            "email": fields.String(required=True, description="user email address"),
            "username": fields.String(required=True, description="user username"),
            "created_at": fields.DateTime(description="user created at"),
            "updated_at": fields.DateTime(description="user updated at"),
        },
    )
    user_request = api.model(
        "user",
        model={
            "email": fields.String(required=True, description="user email address"),
            "username": fields.String(required=True, description="user username"),
        },
    )
