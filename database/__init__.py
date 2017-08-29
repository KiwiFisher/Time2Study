from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base

db = SQLAlchemy()
Base = declarative_base()
engine = db.create_engine('mysql://admin:sdp@localhost/paper_schema')
conn = engine.connect()


