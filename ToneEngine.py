''' Generate tick when triggered '''
from TrackStream import BarTickSound
import pyglet
from pyglet.media import Player
import time

from termcolor import colored

class SampleLib:
    def __init__(self):
        pyglet.options['audio'] = ('openal', 'pulse', 'silent')
        self._samples = {4: pyglet.media.load("samples/Normal-4.wav", streaming = False),
            8: pyglet.media.load("samples/Normal-8.wav", streaming = False),
            16: pyglet.media.load("samples/Normal-16.wav", streaming = False),
            32: pyglet.media.load("samples/Normal-32.wav", streaming = False)}

        self._warm_samples = {4: pyglet.media.load("samples/Warn-4.wav", streaming = False),
            8: pyglet.media.load("samples/Warn-8.wav", streaming = False),
            16: pyglet.media.load("samples/Warn-16.wav", streaming = False),
            32: pyglet.media.load("samples/Warn-32.wav", streaming = False)}

        self._first_sample = pyglet.media.load("samples/First.wav", streaming = False)
        self._pause_sample = pyglet.media.load("samples/Pause.wav", streaming = False)


    def play(self, division, firstInBar, barTick = BarTickSound.NORMAL):
        if firstInBar:
            self._first_sample.play()
        elif barTick == BarTickSound.WARN:
            self._warm_samples[division].play()
        elif barTick == BarTickSound.PAUSE:
            self._pause_sample.play()
        else:
            self._samples[division].play()

class ToneEngine:
    def __init__(self):
        self._sample_lib = SampleLib()

    def doTick(self, note, isFirstInBar, barTick = BarTickSound.NORMAL):
        if note != None:
            self._sample_lib.play(note, isFirstInBar, barTick)
            if isFirstInBar:
                print(colored(str(note) + " " + str(barTick), 'red'))
            else:
                print(str(note) + " " + str(barTick))