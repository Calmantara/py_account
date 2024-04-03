from app.main.model.user import User
from app.main import db
from flask import Flask
from flask.testing import FlaskClient

import json, datetime


def test_get_user(client: FlaskClient, app: Flask):
    # set mock
    user = User(username="username", email="email", password="password")
    user.set_updated_at(datetime.datetime.utcnow())
    user.set_created_at(datetime.datetime.utcnow())
    db.session.add(user)
    db.session.commit()

    response = client.get("/users")
    data = response.get_json()

    with app.app_context():
        assert response.status_code == 200
        assert len(data["data"]) == 1


def test_get_user_by_id(client: FlaskClient, app: Flask):
    # set mock
    user = User(username="username", email="email", password="password")
    user.set_updated_at(datetime.datetime.utcnow())
    user.set_created_at(datetime.datetime.utcnow())
    db.session.add(user)
    db.session.commit()

    usr = User.query.filter_by(username="username").first()

    response = client.get("/users/" + str(usr.id))
    data = response.get_json()

    with app.app_context():
        assert response.status_code == 200
        assert data["data"]["username"] == usr.username
        assert data["data"]["email"] == usr.email


def test_create_user(client: FlaskClient, app: Flask):
    response = client.post(
        "/users",
        data=json.dumps(
            {
                "username": "username1",
                "email": "email@mail.com",
                "password": "password",
            }
        ),
        headers={"Content-Type": "application/json"},
    )
    with app.app_context():
        assert User.query.count() == 1
        assert User.query.first().email == "email@mail.com"
    assert response.status_code == 201
