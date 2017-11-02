import os

"""
This class configured the preset values for our flask app for normal use
"""
class Config(object):

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
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://user:STim3ness@time2.study/Time2'

    @staticmethod
    def from_data(config):
        pass
