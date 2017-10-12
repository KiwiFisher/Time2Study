from structs import Paper, Stream, Lecture
from utils import get_paper_info
from itertools import product

# The algorithm is being designed with modularity in mind. This will allow us to directly interchange algorithms
# should a large scale rebuild ever be required. It also means multiple people could work towards the same goal
# as to find more than one option.


# Here the same json data posted by flask is passed as a list of dictionaries. The presets
# will have have a @TODO defined naming schedule and will be the key in a dictionary with their corresponding value

class Algorithm:
    def __init__(self, papers, presets=None):
        self.papers = {}
        if presets is None:
            presets = {}


        for paper in papers.split(','):
            paper_json = get_paper_info(paper)
            # print(paper_json['streams'])
            streams = {}

            for stream in paper_json['streams']:
                lectures = []
                for lecture in paper_json['streams']['{}'.format(stream)]:

                    # Use this triple for-loop to build up objects from the inside out
                    # Use this indentation for lecture things
                    lectures.append(Lecture(lecture['day'], lecture['room'], lecture['start_time'], lecture['end_time'], lecture['start_date']))

                # Use this indentation for stream things
                streams[stream] = Stream(stream, lectures)

            # Use this indentation for paper things
            self.papers['{}'.format(paper_json['paper_id'])] = Paper(paper_json['paper_id'], paper_json['paper_name'],
                                                                     paper_json['paper_desc'], streams, paper_json['points'],
                                                                     paper_json['level'], paper_json['efts'])



    """
    Match streams will return a list of lists for streams. Each of these
     first list items is a 'timetable'
     """
    def match_streams(self):

        all_paper_streams = []

        for paper in self.papers:
            paper = self.papers[paper]
            paper_streams = []
            for stream in paper.streams:
                stream = paper.streams[stream]
                paper_streams.append({paper.paper_id : stream.steam_id})

            all_paper_streams.append(paper_streams)

        stream_combos = list(product(*all_paper_streams))

        return (stream_combos)
