''' Generate tick when triggered '''
import TrackStream
import pyglet
import time

from termcolor import colored

class SampleLib:
    def __enter__(self):
        pyglet.options['audio'] = ('openal', 'pulse', 'silent')
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
    def __init__(self):
        pass

    def doTick(self, note, isFirstInBar, isEnd):
        if note != None:
            if isFirstInBar:
                print(colored(str(note) + " " + str(isEnd), 'red'))
            else:
                print(str(note) + " " + str(isEnd))