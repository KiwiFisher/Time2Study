import time

# Use of the below classes will allow for easy access of paper information for
# use in the algorithm
class Paper:
    def __init__(self, paper_id, paper_name, paper_desc, streams, points, level, efts):
        self.paper_id = paper_id
        self.paper_name = paper_name
        self.paper_desc = paper_desc
        self.streams = streams
        self.points = points
        self.level = level
        self.efts = efts

    def __str__(self):
        return "{} - ({})".format(self.paper_name, self.paper_id)


# A stream holds a list of lectures and a stream ID
class Stream:
    def __init__(self, stream_id, lectures):
        self.steam_id = stream_id
        self.lectures = lectures

    def __str__(self):
        return "{} - ({} classes)".format(self.steam_id, len(self.lectures))

# A lecture object holds info for one lecture of a stream of a paper. Smallest atom
class Lecture:
    def __init__(self, day, room, start_time, end_time, start_date):
        self.day = time.strptime(day, "%a")
        self.room = room
        self.start_time = time.strptime(start_time, "%H:%M:%S")
        self.end_time = time.strptime(end_time, "%H:%M:%S")
        self.start_date = time.strptime(start_date, "%Y-%m-%d")

    def __str__(self):
        return "{} {} - {} in {}".format(time.strftime("%A", self.day), time.strftime(("%I:%M%p"), self.start_time), time.strftime(("%I:%M%p"), self.end_time), self.room)