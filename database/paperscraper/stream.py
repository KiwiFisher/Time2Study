class stream:
    paper_number = ""
    stream = ""
    lectures = ()

    def __init__(self, stream, paper_number):
        self.stream = stream
        self.paper_number = paper_number

    def add_lecture(self, lecture):
        self.lectures += (lecture, )

    def get_lectures(self):
        return self.lectures

    def __str__(self):
        return self.paper_number + "/" + self.stream