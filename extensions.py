import flask_migrate
from flask_sqlalchemy import SQLAlchemy

"""
Creates a database object for sql alchemy and a migration object for flask migrations
"""

db = SQLAlchemy()
migrate = flask_migrate.Migrate()
