from flask import Flask
from config import config

import os


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init(app)

    #register other modules here

    return app