import pytest

from app.main import create_app, db
from app import blueprint

from flask import Flask
from flask.testing import FlaskClient


@pytest.fixture()
def app() -> Flask:
    # function yang akan digunakan
    # untuk create flask APP dan init db

    # before test
    app, config = create_app(env="test")
    app.register_blueprint(blueprint=blueprint)
    app.app_context().push()

    # when test
    with app.app_context():
        # migrate db
        db.create_all()
    yield app

    # after test
    db.drop_all()


@pytest.fixture()
def client(app: Flask) -> FlaskClient:
    return app.test_client()
