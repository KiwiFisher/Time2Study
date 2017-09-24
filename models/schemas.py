from marshmallow import Schema
from marshmallow import fields

from models import Paper, Stream, Lecture


class PaperSchema(Schema):
    class Meta(Schema):
        model = Paper
        exclude = ('paper_id', 'updated_at', 'created_at')

    paper_id = fields.Str()
    paper_name = fields.Str()
    paper_desc = fields.Str()
    efts = fields.Float()
    level = fields.Int()
    model = fields.Str()


class StreamSchema(Schema):
    class Meta(Schema):
        model = Stream
        exclude = ('updated_at', 'created_at')

    paper_id = fields.Str()
    stream_id = fields.Str()



class LectureSchema(Schema):
    class Meta(Schema):
        model = Lecture
        exclude = ('updated_at', 'created_at')

    paper_id = fields.Str()
    stream_id = fields.Str()
    room = fields.Str()
    start_time = fields.Time()
    end_time = fields.Time()
    start_date = fields.Date()
    day = fields.Str()
