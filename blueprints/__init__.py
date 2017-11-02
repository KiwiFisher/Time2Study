from flask import render_template
from flask_classful import FlaskView
from models import Paper, Stream, Lecture
from .api import ApiView


def home_view():
    papers = Paper.query.all()

    paper_data = [{'paper_id' : paper.paper_id, 'paper_name' : paper.paper_name} for paper in papers]
    print(paper_data)
    return render_template("index.html", _paper_data=paper_data, )


class HomeView(FlaskView):
    route_base = '/'

    def index(self):
        return home_view()