from database import db, conn

class Stream(db.Model):
    __tablename__ = 'stream'
    paper_id = db.Column('paper_id', db.VARCHAR, primary_key=True)
    stream_id = db.Column('stream_id', db.VARCHAR, primary_key=True)