from app.main.model.user import User

import datetime


def test_new_user():
    user = User(username="username", email="email@mail.com", password="password")
    # validation
    assert "username" == user.username
    assert "email@mail.com" == user.email
    assert "password" == user.password


def test_user_created_at():
    user = User(username="username", email="email@mail.com", password="password")
    tn = datetime.datetime.now()
    user.set_created_at(time=tn)
    assert tn == user.created_at


def test_user_updated_at():
    user = User(username="username", email="email@mail.com", password="password")
    tn = datetime.datetime.now()
    user.set_updated_at(time=tn)
    assert tn == user.updated_at
