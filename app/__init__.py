from flask_restx import Api
from flask import Blueprint

from app.main.controller.user import api as user_ns

blueprint = Blueprint("api", __name__)

api = Api(
    blueprint,
    title="Flask Account",
    version="1.0",
    description="a flask account handler",
)
api.add_namespace(user_ns, path="/users")
