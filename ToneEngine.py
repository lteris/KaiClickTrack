''' Generate tick when triggered '''
import TrackStream
import wave
import pyglet

class SampleLib:
    def __enter__(self):
        self.samples = [pyglet.resource.media("samples/Cowbell-1.wav", streaming = False),
            pyglet.resource.media("samples/Cowbell-2.wav", streaming = False),
            pyglet.resource.media("samples/Cowbell-3.wav", streaming = False),
            pyglet.resource.media("samples/Cowbell-4.wav", streaming = False)]

        return self

    def play(self, division):
        if 0 <= division < 4:
            self.samples[division].play()

    def __exit__(self, exc_type, exc_val, exc_tb):
        #do nothing
        pass

class ToneEngine:
    def __init__(self, stream):
        self.stream = stream
        self.__loadTrack()

    def __loadTrack(self):
        pass

    def doTick(self):
        pyglet.options['audio'] = ('openal', 'pulse', 'silent')
        sound = pyglet.resource.media("samples/Cowbell-1.wav", streaming=False)
        sound.play()
        #with SampleLib() as samples:
        #    samples.play(0)

