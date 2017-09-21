from flask import render_template
from flask_classful import FlaskView
from models import Paper, Stream, Lecture
from .api import ApiView


def home_view():
    # papers = Reel.query.all()
    #
    # reel_data = [reel.to_dict() for reel in reels]
    # mono_data = [mono.to_dict() for mono in lines if mono.type == "MONO"]
    # braid_data = [braid.to_dict() for braid in lines if braid.type == "BRAID"]
    #
    # line_brands = set([line.brand for line in lines])
    # reel_brands = set([reel.brand for reel in reels])

    # return render_template("index.html", braid_lines=braid_data, mono_lines=mono_data, reel_data=reel_data,
    #                        line_brands=line_brands, reel_brands=reel_brands)

    return render_template("index.html")


class HomeView(FlaskView):
    route_base = '/'

    def index(self):
        return render_template('index.html')
        # reels = Reel.query.all()
        # lines = Line.query.all()
        #
        # reel_data = {}
        #
        # for reel in reels:
        #     if reel.brand in reel_data.keys():
        #         reel_data[reel.brand].append(reel.to_dict())
        #         continue
        #     reel_data[reel.brand] = [reel.to_dict()]
        #
        # line_data = {
        #     'MONO': {},
        #     'BRAID': {}
        # }
        #
        # for line in lines:
        #     if line.brand is None or line.brand.lower() == 'none':
        #         continue
        #
        #     if line.brand not in line_data[line.type].keys():
        #         line_data[line.type][line.brand] = [line.to_dict()]
        #         continue
        #
        #     line_data[line.type][line.brand].append(line.to_dict())
        #
        # return render_template("index.html", braid_lines=line_data['BRAID'], mono_lines=line_data['MONO'],
        #                        reel_data=reel_data)
