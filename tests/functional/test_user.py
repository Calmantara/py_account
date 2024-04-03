# testing for /users API

from flask import Flask
from flask.testing import FlaskClient
from app.main.model.user import User
from app.main import db

import datetime, json


def test_get_users(app: Flask, client: FlaskClient):
    # before
    # seeding 1 mock data to database first
    tn = datetime.datetime.utcnow()
    user = User(username="", email="", password="")
    user.set_created_at(tn)
    user.set_updated_at(tn)
    db.session.add(user)
    db.session.commit()

    # when
    # test hit API /users
    # response -> list of users
    resp = client.get("/users")
    data = resp.get_json()
    with app.app_context():
        assert resp.status_code == 200
        assert len(data["data"]) == 1


def test_create_users(app: Flask, client: FlaskClient):
    resp = client.post(
        "/users",
        data=json.dumps(
            {
                "username": "username3",
                "email": "email3@mail.com",
                "password": "password2",
            }
        ),
        headers={"Content-Type": "application/json"},
    )
    with app.app_context():
        assert resp.status_code == 201
        # testing data in database
        assert User.query.count() == 1
        assert User.query.first().username == "username3"
        assert User.query.first().email == "email3@mail.com"


def test_get_users_detail(app: Flask, client: FlaskClient):
    # before
    # seeding 1 mock data to database first
    tn = datetime.datetime.utcnow()
    user = User(username="username", email="email@mail.com", password="")
    user.set_created_at(tn)
    user.set_updated_at(tn)
    db.session.add(user)
    db.session.commit()
    # query inputted user
    input_user = User.query.filter_by(username="username").first()

    # when
    # test hit API /users
    # response -> list of users
    resp = client.get("/users/" + str(input_user.id))
    data = resp.get_json()
    with app.app_context():
        assert resp.status_code == 200
        assert data["data"]["username"] == input_user.username
        assert data["data"]["email"] == input_user.email
        assert data["data"]["id"] == input_user.id


# challenge:
# buat test untuk delete user
