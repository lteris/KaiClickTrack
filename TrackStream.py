''' Load configuration from json input file '''

import json

class TrackStream:

    def __init__(self, file):
        self.track = json.load(file)

    