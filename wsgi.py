from werkzeug.serving import run_simple
from werkzeug.wsgi import DispatcherMiddleware
from config import Config
from factory import create_app

"""
This call will create and set up the flask app without running it
"""
application = DispatcherMiddleware(create_app(settings=Config))

"""
If this class is run directly, then start the flask app with the debugger and reloader
0.0.0.0 means it is externally visible, 5000 is the port, APPLICATION is the flask app

run_simple is a method from werkzueg, a WSGI utility library. It lets us
"""
if __name__ == "__main__":
    run_simple('127.0.0.1', 5000, application, use_reloader=True, use_debugger=True)


