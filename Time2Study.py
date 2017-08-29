from flask import Flask
from flask import render_template
from flask_jsonpify import jsonpify
from database import db
from database.models import Paper

"""
Welcome to Time2Study. This Flask app will take the pain out of enrolling at AUT through the dinosaur that is Arion.

html files can be found in templates
css and javvascript files can be found in static along with other static assets
sqlalchemy bits nd ORM models can be found in database and database/models
"""

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://admin:sdp@localhost/paper_schema'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/api/info/<paper_id>')
def paper_info(paper_id):
    return jsonpify(Paper.get_info(paper_id))


@app.route("/api/algorithm/<path:papers_string>")
def api(papers_string):
    papers = papers_string.split("/")
    return str(papers)

if __name__ == '__main__':
    app.run()