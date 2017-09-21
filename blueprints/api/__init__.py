from flask import jsonify, request
from flask_classful import FlaskView, route

from marshmallow import fields

from webargs.flaskparser import use_args


from models import Paper, Stream, Lecture
from utils import output_json
import ast


"""
The ApiView sets up the POST points for interaction with the API
JSON data can be posted to the api index and a response will be sent with the
appropriate data"""
class ApiView(FlaskView):
    route_base = '/api/'
    representations = {'application/json': output_json}

    @route("/", methods=['POST', 'GET'])
    def index(self):
        if request.method == 'GET':
            print(Paper.get_by_id('COMP603'))
            return jsonify({'API' : 'Time2Study', 'version' : '0.1a'})

        elif request.method == 'POST':
            args = ast.literal_eval(list(request.form)[0])
            reel_id = args['reel_id']
            known_line_id = args['known_line_id']
            known_line_length = args['known_line_length']
            unknown_line_id = args['unknown_line_id']
            reel = Reel.get_by_id(reel_id)
            known_line = Line.get_by_id(known_line_id)
            unknown_line = Line.get_by_id(unknown_line_id)

            if reel is None or known_line is None or unknown_line is None:
                return jsonify({
                    'error': 'Unable to perform request'
                })

            known_volume = utils.calculate_volume(known_line.diameter, known_line.packing, known_line_length)
            unknown_vol = float(reel.volume) - float(known_volume)

            return jsonify(
                {'length': round(utils.get_line_length(unknown_vol, unknown_line.diameter, unknown_line.packing), 1)})

