''' Generate tick when triggered '''
import TrackStream
import wave
import pyglet

class SampleLib:
    def __enter__(self):
        self.samples[0] = pyglet.resource.media("samples/Cowbell-1.wav", streaming = False)
        self.samples[1] = pyglet.resource.media("samples/Cowbell-2.wav", streaming = False)
        self.samples[2] = pyglet.resource.media("samples/Cowbell-3.wav", streaming = False)
        self.samples[3] = pyglet.resource.media("samples/Cowbell-4.wav", streaming = False)

        return self

    def play(self, division):
        if 0 <= division < 4:
            self.samples[division].play()

    def __exit__(self, exc_type, exc_val, exc_tb):
        for f in self.samples:
            f.close()

class ToneEngine:

    def __init__(self, stream):
        self.stream = stream
        self.__load_track()

    def __loadTrack(self):
        pass

    def doTick(self):
        with SampleLib() as samples:
            samples.play(0)

