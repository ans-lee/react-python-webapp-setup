from flask import Flask

from api.model import db


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object('api.config.Config')
    db.init_app(app)

    with app.app_context():
        db.create_all()
        return app
