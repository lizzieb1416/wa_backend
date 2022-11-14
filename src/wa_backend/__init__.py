from __future__ import annotations

__version__ = "0.1.1"

import logging
# from flask import Flask, request, jsonify
# from flask_sqlalchemy import SQLAlchemy
# from flask_cors import CORS
# import json
from os import environ

from flask import Flask

from .apis.tasks import blueprint as bp_tasks
from .apis.tasks import db as db_tasks



def create_app():
    app = Flask(__name__)
    
    app.config["SQLALCHEMY_DATABASE_URI"] = environ.get(
    "DATABASE_URL", "sqlite:///database.db"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = "False"
    
    @app.route('/')
    def hello():
        return "youpi"
    
    # registering blueprint
    app.register_blueprint(bp_tasks)
    db_tasks.init_app(app)
    
    return app    


if __name__ == '__main__':
    app = create_app()
    app.run()

