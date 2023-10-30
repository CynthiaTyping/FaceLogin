import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploads/')
db = SQLAlchemy()


class CfgClass():
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:123@localhost:3306/db5"


def create_app():
    from .model import Users
    app = Flask(__name__)
    app.config.from_object(CfgClass)
    db.init_app(app)
    from .web import web as web_blueprint
    app.register_blueprint(web_blueprint)
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.secret_key = 'secret_key_here'
    return app
