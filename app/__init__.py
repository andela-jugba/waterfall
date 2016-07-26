from flask import Flask
from config import config
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

bootstrap = Bootstrap()
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init(app)

    #register other modules here
    bootstrap.init_app(app)
    db.init_app(app)

    #register blueprints here
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app