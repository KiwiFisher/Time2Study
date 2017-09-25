from flask import render_template
from flask_classful import FlaskView
from models import Paper, Stream, Lecture
from .api import ApiView


def home_view():

    return render_template("index.html")


class HomeView(FlaskView):
    route_base = '/'

    def index(self):
        return home_view()