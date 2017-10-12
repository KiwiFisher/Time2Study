from flask import jsonify, request
from flask_classful import FlaskView, route
from models import Paper, Stream, Lecture
from utils import output_json
from algorithm import Algorithm
from utils import get_paper_info



class ApiView(FlaskView):
    """
    The ApiView sets up the POST points for interaction with the API
    JSON data can be posted to the api index and a response will be sent with the
    appropriate data
    """
    route_base = '/api/'
    representations = {'application/json': output_json}

    @route("/", methods=['POST', 'GET'])
    def index(self):
        if request.method == 'GET':

            return jsonify({'API' : 'Time2Study', 'version' : '0.1a'})

        elif request.method == 'POST':
            """
            If it's a post request then we are expected to respond with some info
            """
            request_type = request.args.to_dict()['request']

            if request_type == 'info':
                return jsonify(get_paper_info(request.args.to_dict()['paper_id']))

            elif request_type == 'algorithm':
                papers = request.args.to_dict()['papers']
                return jsonify(Algorithm(papers).match_streams())

            else:
                return 'INVALID API USAGE'

