# code untuk loading config
# .env
# config.yaml

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "my_precious_secret_key")
    APP_NAME = os.getenv("APP_NAME", "py-project-structure")
    APP_PORT = os.getenv("APP_PORT", 5000)
    DEBUG = os.getenv("DEBUG", False)


# class Development(Config):
#     SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "py_account.db")
#     SQLALCHEMY_ECHO = True
#     SQLALCHEMY_TRACK_MODIFICATIONS = False


class Development(Config):
    postgres_password = os.getenv("POSTGRES_PASSWORD")
    postgres_username = os.getenv("POSTGRES_USERNAME")
    postgres_host = os.getenv("POSTGRES_HOST")

    SQLALCHEMY_DATABASE_URI = (
        "postgresql://"
        + postgres_username
        + ":"
        + postgres_password
        + "@"
        + postgres_host
        + "/py_account"
    )
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


# class Production(Config):
#     SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "py_account.db")
#     SQLALCHEMY_ECHO = False
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
class Production(Config):
    postgres_password = os.getenv("POSTGRES_PASSWORD")
    postgres_username = os.getenv("POSTGRES_USERNAME")
    postgres_host = os.getenv("POSTGRES_HOST")

    SQLALCHEMY_DATABASE_URI = (
        "postgresql://"
        + postgres_username
        + ":"
        + postgres_password
        + "@"
        + postgres_host
        + "/py_account"
    )
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config_env = dict(development=Development, production=Production)
