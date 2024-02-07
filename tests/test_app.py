import pytest


from .app import User, UserManager


def test_add_user(db):
    user = User(name="Hello World")
    db.session.add(user)
    db.session.commit()

    user = db.session.query(User).one()
    assert user and user.id and user.name == "Hello World"


def test_add_user_with_user_manager(db):
    user = UserManager().create(name="Hello Managed", commit=True)
    assert user and user.id and user.name == "Hello Managed"

    user2 = User.query.filter_by(name="Hello Managed").one()
    assert user == user2
