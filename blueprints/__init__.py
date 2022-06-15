from blueprints.users import users_api


def register_blueprints(app):
    app.register_blueprint(users_api)
