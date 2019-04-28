''' Generate tick when triggered '''
import TrackStream
import pyglet
import time

from termcolor import colored

class SampleLib:
    def __init__(self):
        pyglet.options['audio'] = ('openal', 'pulse', 'silent')
        self._samples = {4: pyglet.resource.media("samples/Cowbell-1.wav", streaming = False),
            8: pyglet.resource.media("samples/Cowbell-2.wav", streaming = False),
            16: pyglet.resource.media("samples/Cowbell-3.wav", streaming = False),
            32: pyglet.resource.media("samples/Cowbell-4.wav", streaming = False)}

        self._warm_samples = {4: pyglet.resource.media("samples/Klank-1.wav", streaming = False),
            8: pyglet.resource.media("samples/Klank-2.wav", streaming = False),
            16: pyglet.resource.media("samples/Klank-3.wav", streaming = False),
            32: pyglet.resource.media("samples/Klank-4.wav", streaming = False)}

        self._first_sample = pyglet.resource.media("samples/Klank-6.wav", streaming = False)

    def play(self, division, firstInBar, warnEnd):
        if firstInBar:
            self._first_sample.play()
        elif warnEnd:
            self._warm_samples[division].play()
        else:
            self._samples[division].play()

class ToneEngine:
    def __init__(self):
        self._sample_lib = SampleLib()

    def doTick(self, note, isFirstInBar, isEnd):
        if note != None:
            self._sample_lib.play(note, isFirstInBar, isEnd)
            if isFirstInBar:
                print(colored(str(note) + " " + str(isEnd), 'red'))
            else:
                print(str(note) + " " + str(isEnd))