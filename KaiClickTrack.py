from TrackStream import TrackStream
from ToneEngine import ToneEngine
from GraphicsEngine import GraphicsEngine
from PulseGenerator import PulseGenerator

import sys

if __name__ == "__main__":
    file = "saga.json"
    if len(sys.argv) < 2:
        print("usage: KaiClickTrack.py <track file>")
    else:
        file = sys.argv[1]

    stream = TrackStream(file)
    graphics = GraphicsEngine(stream)
    tone = ToneEngine(stream)
    pulse = PulseGenerator(stream)

    pulse.addSubscriber([tone, graphics])
    pulse.run()