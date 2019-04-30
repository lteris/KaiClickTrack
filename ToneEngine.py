''' Generate tick when triggered '''
import TrackStream
import pyglet
import time

from termcolor import colored

class SampleLib:
    def __init__(self):
        pyglet.options['audio'] = ('openal', 'pulse', 'silent')
        self._samples = {4: pyglet.resource.media("samples/Normal-4.wav", streaming = False),
            8: pyglet.resource.media("samples/Normal-8.wav", streaming = False),
            16: pyglet.resource.media("samples/Normal-16.wav", streaming = False),
            32: pyglet.resource.media("samples/Normal-32.wav", streaming = False)}

        self._warm_samples = {4: pyglet.resource.media("samples/Warn-4.wav", streaming = False),
            8: pyglet.resource.media("samples/Warn-8.wav", streaming = False),
            16: pyglet.resource.media("samples/Warn-16.wav", streaming = False),
            32: pyglet.resource.media("samples/Warn-32.wav", streaming = False)}

        self._first_sample = pyglet.resource.media("samples/First.wav", streaming = False)
        self._pause_sample = pyglet.resource.media("samples/Pause.wav", streaming = False)

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