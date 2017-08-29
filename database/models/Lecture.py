from database import db, conn

class Lecture:
    __tablename__ = 'lecture'
    paper_id = db.Column('paper_id', db.VARCHAR)
    stream_id = db.Column('stream_id', db.VARCHAR)
    room = db.Column('room', db.VARCHAR)
    start_time = db.Column('start_time', db.TIME)
    end_time = db.Column('end_time', db.TIME)
    start_date = db.Column('start_date', db.DATE)
    day = db.Column('day', db.VARCHAR)