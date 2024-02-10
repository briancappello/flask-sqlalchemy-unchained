from flask import Flask

from flask_sqlalchemy_unchained import ModelManager, SQLAlchemyUnchained


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
db = SQLAlchemyUnchained(app)


class User(db.Model):  # type: ignore[name-defined]
    class Meta:
        repr = ("id", "name")

    name = db.Column(db.String)


class UserManager(ModelManager):
    class Meta:
        model = User
