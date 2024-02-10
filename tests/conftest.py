import typing as t

import pytest

from flask import Flask

from flask_sqlalchemy_unchained import SQLAlchemyUnchained


@pytest.fixture(autouse=True)
def app() -> t.Generator[Flask, None, None]:
    from .app import app

    with app.app_context():
        yield app


@pytest.fixture()
def db() -> t.Generator[SQLAlchemyUnchained, None, None]:
    from .app import db

    db.create_all()

    yield db
