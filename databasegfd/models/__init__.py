from database import db, Session, Base
from sqlalchemy import Column, Integer, String, Float, Time, Date, inspect


# This class models a paper for SQLAlchemy
class Paper(Base):
    __tablename__ = 'paper'
    paper_id = Column('paper_id', String, primary_key=True)
    paper_name = Column('paper_name', String)
    paper_desc = Column('paper_desc', String)
    efts = Column('efts', Float)
    points = Column('points', Float)
    level = Column('level', Integer)

    def get_info(paper_id):
        """
        Gets all available information on a given paper
        :return: A dictionary containing all paper information
        """
        session = Session()

        info = {}

        for paper in session.query(Paper).filter_by(paper_id=paper_id):

            info['paper_id'] = paper.paper_id
            info['paper_name'] = paper.paper_name
            info['paper_desc'] = paper.paper_desc
            info['efts'] = paper.efts
            info['points'] = paper.points
            info['level'] = paper.level

            info['streams'] = {}

            for lecture in session.query(Lecture).filter_by(paper_id=paper_id):
                if lecture.stream_id not in info['streams']:
                    info['streams'][lecture.stream_id] = []

                lec_info = {'room': lecture.room, 'day': str(lecture.day),
                            'start_time': str(lecture.start_time), 'end_time': str(lecture.end_time),
                            'start_date': str(lecture.start_date)}

                info['streams'][lecture.stream_id].append(lec_info)

        session.close()
        return info



class Lecture(Base):
    __tablename__ = 'lecture'
    paper_id = Column('paper_id', String, primary_key=True)
    stream_id = Column('stream_id', String, primary_key=True)
    room = Column('room', String, primary_key=True)
    start_time = Column('start_time', Time, primary_key=True)
    end_time = Column('end_time', Time)
    start_date = Column('start_date', Date, primary_key=True)
    day = Column('day', String, primary_key=True)


class Stream(Base):
    __tablename__ = 'stream'
    paper_id = db.Column('paper_id', Integer, primary_key=True)
    stream_id = db.Column('stream_id', Integer, primary_key=True)
