from algorithm.objectify import Paper, Stream, Lecture

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


        for paper in papers:
            streams = {}

            for stream in paper['streams']:
                lectures = []
                for lecture in paper['streams']['{}'.format(stream)]:
                    # Use this triple for-loop to build up objects from the inside out
                    # Use this indentation for lecture things
                    lectures.append(Lecture(lecture['day'], lecture['room'], lecture['start_time'], lecture['end_time'], lecture['start_date']))

                # Use this indentation for stream things
                streams[stream] = Stream(stream, lectures)

            # Use this indentation for paper things
            self.papers['{}'.format(paper['paper_id'])] = Paper(paper['paper_id'], paper['paper_name'],
                                                                paper['paper_desc'], streams, paper['points'],
                                                                paper['level'], paper['efts'])



    def match_streams(self):
        to_return = {}

        for paper_id in self.papers:
            paper = self.papers[paper_id]
            print(paper)
            to_return[paper.paper_id] = paper.paper_name

            for stream_id in paper.streams:
                stream = paper.streams[stream_id]
                print("    - " + str(stream))

                for lecture in stream.lectures:
                    print("        - " + str(lecture))

        return to_return

    # def match_streams(self):
    #     to_return = {}
    #
    #     # Your code here
    #
    #     return to_return
