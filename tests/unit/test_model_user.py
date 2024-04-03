from app.main.model.user import User


def test_new_user():
    user = User("username", "mail@mail.com", "password")
    assert user.email == "mail@mail.com"
    assert user.username == "username"
    assert user.password == "password"
