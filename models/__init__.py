from extensions import db


class Paper(db.Model):
    """
    The Paper class is designed to model the mysql database which stores all of the paper information.

    Through use of flask-sqlalchemy the model instructs python to create a Paper object with the values
    named in the model and the value from each column of a row.
    """

    # Models the 'paper' table
    __tablename__ = 'paper'

    # The variable names on the left is the name of the variabvle in the object.
    # The assigned value is the column from which the information is to be retrieved from
    paper_id = db.Column(db.Integer, primary_key=True)
    paper_name = db.Column(db.Unicode)
    paper_desc = db.Column(db.Unicode)
    efts = db.Column(db.Float)
    points = db.Column(db.Integer)
    level = db.Column(db.Float)


    def to_dict(self):
        """
        This will turn all the information for a paper in to a dictionary
        Given that the paper table doesn't have stream or lecture info, we must append that
        :return: DIctionary of all information in the database on a given paper
        """

        info = dict(
            paper_id=self.paper_id,
            paper_name=self.paper_name,
            paper_desc=self.paper_desc,
            streams={},
            efts=self.efts,
            points=self.points,
            level=self.level,
        )

        """
        This add on part adds all of the stream and lecture information in too to avoid having to  make
        separate calls and then merge the two
        """
        for lecture in Lecture.query.filter_by(paper_id=self.paper_id):
            if lecture.stream_id not in info['streams']:
                info['streams'][lecture.stream_id] = []

            lec_info = {'room': lecture.room, 'day': str(lecture.day),
                        'start_time': str(lecture.start_time), 'end_time': str(lecture.end_time),
                        'start_date': str(lecture.start_date)}

            info['streams'][lecture.stream_id].append(lec_info)

        return info



class Stream(db.Model):
    """
    The Stream class models the lecture table
    """

    __tablename__ = 'stream'

    paper_id = db.Column(db.Unicode, primary_key=True)
    stream_id = db.Column(db.Unicode, primary_key=True)

    def to_dict(self):
        return dict(
            paper_id=self.paper_id,
            stream_id=self.stream_id,
        )


class Lecture(db.Model):
    """
    The Lecture class models the lecture table
    """
    __tablename__ = 'lecture'

    paper_id = db.Column(db.Unicode, primary_key=True)
    stream_id = db.Column(db.Unicode, primary_key=True)
    room = db.Column(db.Unicode, primary_key=True)
    start_time = db.Column(db.Unicode, primary_key=True)
    end_time = db.Column(db.Unicode)
    start_date = db.Column(db.Unicode, primary_key=True)
    day = db.Column(db.Unicode, primary_key=True)


    def to_dict(self):
        return dict(
            paper_id=self.paper_id,
            stream_id=self.stream_id,
            room=self.room,
            start_time=self.start_time,
            end_time=self.end_time,
            start_date=self.start_date,
            day=self.day
        )

