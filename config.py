import os


class Config(object):
    """
        Base Configuration for Flask (spool-wizard)
        """

    ENV = None

    PROJECT = "time2study"

    PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    ADMINS = ['julian.abraham97@gmail.com']

    INSTANCE_FOLDER_PATH = os.getcwd()

    LOG_FOLDER = os.path.join(INSTANCE_FOLDER_PATH, 'logs')
    LOGGING = False

    DEBUG = False
    TESTING = False

    # Flask Debug-Toolbar Settings
    ASSETS_DEBUG = False
    DEBUG_TB_ENABLED = False  # Disable Debug toolbar
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    # SQLAlchemy Settings
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DATABASE_NAME = 'application.db'
    DATABASE_PATH = os.path.join(INSTANCE_FOLDER_PATH, DATABASE_NAME)
    SQLALCHEMY_DATABASE_URI = 'mysql://admin:sdp@localhost/paper_schema'

    @staticmethod
    def from_data(config):
        pass


class DevConfig(Config):
    ENV = None

    PROJECT = "time2study"

    PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    ADMINS = ['julian.abraham97@gmail.com']

    INSTANCE_FOLDER_PATH = os.path.join(os.path.expanduser("~"), '/Projects/Python/time2study/')

    LOG_FOLDER = os.path.join(INSTANCE_FOLDER_PATH, 'logs')
    LOGGING = False

    DEBUG = False
    TESTING = False

    # Flask Debug-Toolbar Settings
    ASSETS_DEBUG = False
    DEBUG_TB_ENABLED = False  # Disable Debug toolbar
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    # SQLAlchemy Settings
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DATABASE_NAME = 'application.db'
    DATABASE_PATH = os.path.join(INSTANCE_FOLDER_PATH, DATABASE_NAME)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}'.format(Config.DATABASE_PATH)
