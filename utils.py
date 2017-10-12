from flask import json
from flask import make_response
from models import Paper
from flask import request
from flask import jsonify


"""
This defines the layout of json response used in the API view for responding to ajax posts"""
def output_json(data, code, headers=None):
    content_type = 'application/json'
    dumped = json.dumps(data)
    if headers:
        headers.update({'Content-Type': content_type})
    else:
        headers = {'Content-Type': content_type}
    response = make_response(dumped, code, headers)
    return response

def get_paper_info(paper_id):
    paper = Paper.query.filter_by(paper_id=paper_id).first()
    if paper is not None:
        return paper.to_dict()
    else:
        return 'INVALID PAPER_ID'