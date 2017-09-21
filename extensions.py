import flask_migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = flask_migrate.Migrate()
