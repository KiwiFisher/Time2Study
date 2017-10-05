from selenium import webdriver
from bs4 import BeautifulSoup as BS

class paper:
    code = ""
    name = ""
    link = ""
    prescriptor = ""
    efts = ""
    points = ""
    level = ""
    timetable = {}

    def __init__(self, code, name, link):
        self.code = code
        self.name = name
        self.link = link

    def collect_data(self):
        # no classes for invalid codes
        if self.name == "INVALID CODE":
            return {}

        driver = webdriver.PhantomJS()

        # open a client
        driver.get(self.link)

        html_source = driver.page_source

        # close the window
        driver.close()

        soup = BS(html_source, "html.parser")

        class_times = soup.findAll("tr", {"class": "BackgroundLight"})
        info = soup.findAll("td", {"class": "BackgroundLight"})
        prescriptor_elements = soup.findAll("a", {"name" : "#Prescriptor"})

        self.prescriptor = prescriptor_elements[0].parent.parent.parent.findAll("td", None)[1].getText().strip()
        self.efts = info[1].getText()
        self.points = info[2].getText()
        self.level = info[3].getText()

        current_paper = ""
        current_stream = ""
        streams = {}
        new_stream = False

        # For each of the rows in the table we must iterate through and filter the information into streams and classes
        for i in range(len(class_times)):

            cells = class_times[i].find_all("td")

            # If there is no text in the paper column then it means that its the same as it was before
            # If it does have text it means that it's a new stream
            if len(cells[0].getText()) > 1:
                new_stream = True
                current_paper = cells[0].getText()
                current_stream = cells[1].getText()
                #If we have a new stream within the stream, then create a new stream
            elif len(cells[1].getText()) > 1:
                new_stream = True
                current_stream = cells[1].getText()

            split = (current_paper.strip() + current_stream.strip()).split("/")

            paper_number = split[0]
            paper_stream = split[1]
            starting = cells[2].getText().strip()
            day = cells[3].getText().strip()
            time = cells[4].getText().strip()
            room = cells[5].getText().strip()

            time_split = time.split(" - ")

            if len(time_split) > 1:
                start = time_split[0]
                start_nums = start.split(" ")


                finish = time_split[1]
            else:
                start = ""
                finish = ""

            # if our paper number is the same as current_paper then add to the stream, otherwise make a new stream
            # and update current paper
            if new_stream and len(room) > 1:
                new_stream = False
                streams[paper_stream] = stream(paper_stream, paper_number)



            if len(room) > 1:
                streams[paper_stream].add_lecture(lecture(paper_number, paper_stream, room, day, start, finish, starting))

        self.timetable = streams
