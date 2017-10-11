from flask import Flask, jsonify
from werkzeug.exceptions import default_exceptions, HTTPException

from config import Config

"""
This file has all of the methods needed to generate a fully configured flask app

These are all generic
"""


def make_json_error(ex):
    if hasattr(ex, 'status'):
        status_message = getattr(ex, 'status')

    else:
        status_message = "ERROR"

    response = dict(
        messages=[],
        status=status_message
    )

    to_dict = getattr(ex, 'to_dict', None)  # Check if we can get a dictionary from the error

    if callable(to_dict):
        response.update(to_dict())
    else:
        response['messages'] = str(ex)

    if hasattr(ex, 'exc'):
        for message in ex.exc.messages:
            response['messages'].append(message)

    response = jsonify(response)

    if isinstance(ex, HTTPException) or hasattr(ex, 'code'):
        status_code = ex.code
    else:
        status_code = 400
    response.status_code = status_code

    return response


def register_error_handlers(app: Flask):
    for code in default_exceptions.items():
        app.error_handler_spec[None][code] = make_json_error


def apply_config(app, config):
    app.config.from_object(config)
    return app


def configure_extensions(app: Flask):
    from extensions import db, migrate

    db.init_app(app)
    migrate.init_app(app, db)

    return app


def register_blueprints(app: Flask):
    from blueprints.api import ApiView
    from blueprints import HomeView

    HomeView.register(app)
    ApiView.register(app)

    return app


def create_app(settings=None):
    """
    Creates and returns a fully configured application following the factory pattern.
    :param settings: configuration class (tbd)
    :return: Flask App instance
    """

    app = Flask(
        __name__,
        instance_path=settings.INSTANCE_FOLDER_PATH,
        instance_relative_config=True
    )

    if settings is None:
        settings = Config()

    # See if there are any settings to override.
    apply_config(app, settings)

    # Configure our extensions
    configure_extensions(app)

    # Register application blueprints
    register_blueprints(app)

    # Register error handlers
    register_error_handlers(app)

    return app


def configure_app(app: Flask, config: dict):
    for key, value in config.items():
        app.config[key] = value
