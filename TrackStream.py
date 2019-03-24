''' Load configuration from json input file '''

import json

class TrackStream:

    def __init__(self, file):
        f = open(file, "r")
        self.track = json.load(f)
        # begin at sequnece 0 bar 0
        self.__sequence = 0
        self.__bar = 0

    def advance():
        pass

    def getCurrent():
        pass

    