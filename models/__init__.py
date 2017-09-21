import utils
from database import SqlModel, Column, SurrogatePK
from extensions import db


class Paper(SqlModel, SurrogatePK):
    __tablename__ = 'line'

    paper_id = db.Column(db.Integer, primary_key=True)
    paper_name = db.Column(db.Unicode)
    paper_desc = db.Column(db.Unicode)
    efts = db.Column(db.Float)
    points = db.Column(db.Integer)
    level = db.Column(db.Float)

    def __init__(self, paper_id, paper_name, paper_desc, efts, points, level, **kwargs):
        SqlModel.__init__(
            self,
            paper_id=paper_id,
            paper_name=paper_name,
            paper_desc = paper_desc,
            efts=efts,
            points=points,
            level=level,
            **kwargs
        )

    def to_dict(self):
        return dict(
            paper_id=self.paper_id,
            paper_name=self.paper_name,
            paper_desc=self.paper_desc,
            efts=self.efts,
            points=self.points,
            level=self.level,
        )


class Stream(SqlModel, SurrogatePK):
    __tablename__ = 'stream'

    paper_id = Column(db.Unicode, primary_key=True)
    stream_id = Column(db.Unicode, primary_key=True)

    def __init__(self, paper_id, stream_id, **kwargs):
        SqlModel.__init__(self,
                          paper_id=paper_id, stream_id=stream_id, **kwargs)

    # @property
    # def volume(self):
    #     mono_volume = utils.calculate_volume(Line.get_by_id(self.mono_id).diameter, Line.get_by_id(self.mono_id).packing, self.mono_length)
    #     braid_volume = utils.calculate_volume(Line.get_by_id(self.braid_id).diameter, Line.get_by_id(self.braid_id).packing, self.braid_length)
    #
    #     return mono_volume + braid_volume

    def to_dict(self):
        return dict(
            paper_id=self.paper_id,
            stream_id=self.stream_id,
        )


class Lecture(SqlModel, SurrogatePK):
    __tablename__ = 'lecture'

    paper_id = db.Column(db.Unicode, primary_key=True)
    stream_id = db.Column(db.Unicode, primary_key=True)
    room = db.Column(db.Unicode, primary_key=True)
    start_time = db.Column(db.Unicode, primary_key=True)
    end_time = db.Column(db.Unicode)
    start_date = db.Column(db.Unicode, primary_key=True)


    def __init__(self, paper_id, stream_id, room, start_time, end_time, start_date, **kwargs):
        SqlModel.__init__(
            self,
            paper_id = paper_id,
            stream_id = stream_id,
            room = room,
            start_time = start_time,
            end_time = end_time,
            start_date = start_date,
            **kwargs
        )

    def to_dict(self):
        return dict(
            paper_id=self.paper_id,
            stream_id=self.stream_id,
            room=self.room,
            start_time=self.start_time,
            end_time=self.end_time,
            start_date=self.start_date
        )

