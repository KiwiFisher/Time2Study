from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create the ORM
db = SQLAlchemy()

# Creates a new session
engine = db.create_engine('mysql://admin:sdp@localhost/paper_schema')
Session = sessionmaker(bind=engine)

# Trying to get rod of conn.
conn = engine.connect()

Base = declarative_base()



