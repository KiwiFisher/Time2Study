from flask import jsonify, request
from flask_classful import FlaskView, route
from models import Paper, Stream, Lecture
from utils import output_json


"""
The ApiView sets up the POST points for interaction with the API
JSON data can be posted to the api index and a response will be sent with the
appropriate data
"""
class ApiView(FlaskView):
    route_base = '/api/'
    representations = {'application/json': output_json}

    @route("/", methods=['POST', 'GET'])
    def index(self):
        if request.method == 'GET':

            # return jsonify(Paper.query.filter_by(paper_id='COMP603').first().to_dict())
            return jsonify({'API' : 'Time2Study', 'version' : '0.1a'})

        elif request.method == 'POST':
            #args = ast.literal_eval(list(request.form)[0])
            request_type = request.args.to_dict()['request']

            if request_type == 'info':
                paper = Paper.query.filter_by(paper_id=request.args.to_dict()['paper_id']).first()
                if paper is not None:

                    return jsonify(paper.to_dict())
                else:
                    return jsonify('INVALID PAPER_ID')

            elif request_type == 'algorithm':
                return jsonify({'algorithm' : True})

            else:
                return 'INVALID API USAGE'

