import pytest

from flask import Flask
from app.main import create_app, db
from app import blueprint


@pytest.fixture()
def app() -> Flask:
    app, config = create_app(env="test")
    app.register_blueprint(blueprint=blueprint)
    app.app_context().push()
    with app.app_context():
        db.create_all()
    yield app
    # tear down
    db.drop_all()
    print("DONE")


@pytest.fixture()
def client(app: Flask):
    return app.test_client()
