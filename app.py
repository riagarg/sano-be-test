from flask import Flask

from core.blueprints import register_blueprints
from core.models import create_tables, drop_tables


def create_app():
    app = Flask(__name__)
    register_blueprints(app)

    @app.route("/")
    def hello_world():
        return "<h1>Hi there!</h1>"

    return app

drop_tables()
create_tables()