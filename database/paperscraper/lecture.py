from datetime import datetime

class lecture:
    paper_number = 0
    stream = ""
    room = ""
    starting = datetime
    day = datetime
    start = datetime
    finish = datetime
    time = datetime

    def __init__(self, paper_number, stream, room, day, start, finish, starting):
        self.paper_number = paper_number
        self.stream = stream
        self.room = room
        self.finish = finish
        self.starting = datetime.strptime(starting, "%d-%b-%Y")
        self.day = day
        self.start = datetime.strptime(self.time_to_string(start), "%I:%M%p")
        self.finish = datetime.strptime(self.time_to_string(finish), "%I:%M%p")

    # def __str__(self):
    #     if len(self.room) > 1:
    #         return self.day.strftime("%A") + " " + str(self.start.time()) + " in " + self.room
    #     else:
    #         return "No lecture"

    # This method takes the time given on arion and coverts it in to a string that can be saved as a time
    def time_to_string(self, time):

        time = time.replace(".", "")
        time = time.replace(" ", "")
        time = time.upper()

        return time
