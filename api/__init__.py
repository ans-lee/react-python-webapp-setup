from flask import Flask

from api.model import db

ENVS = {
    'dev': 'api.config.DevelopmentConfig',
    'prod': 'api.config.ProductionConfig',
    'test': 'api.config.TestingConfig'
}

def create_app(env: str) -> Flask:
    app = Flask(__name__)
    app.config.from_object(ENVS[env])
    db.init_app(app)

    with app.app_context():
        db.create_all()
        return app
