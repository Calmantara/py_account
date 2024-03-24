# main module
# load all configs
# and spawn flask

from flask_sqlalchemy import SQLAlchemy
from flask import Flask

from app.main.configuration.config import config_env

db = SQLAlchemy()


def create_app(env: str):
    app = Flask(__name__)
    # class of config
    config = config_env[env]

    # bind config to app
    app.config.from_object(config)
    try:
        db.init_app(app=app)
    except:  # noqa: E722
        raise ("error in init database connection")
    return app, config
