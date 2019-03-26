''' Load configuration from json input file '''

import json

'''click_divide = division of the base note that is not silent; =2 on tempo */4 means play every 8th note
   tick_note = frequency of the pulse - tick_note=16 => every 16th note you get called
   barcount = number of bars in this sequnce

   Return - the type of note to play for every tick_note: 4th, 8th ... or None if the note
   on the current tick is silent. 
'''
def barnotes(barcount, tempo="4/4", click_divide=1, tick_note = 16, warn = False):
    tempo_supra, base_note = map(int, tempo.split("/"))

    #number of ticks in the whole sequence
    ticks_in_sequence= barcount * tempo_supra / base_note * tick_note
    ticks_in_base_note = tick_note / base_note
    
    crt_tick = 0

    # find the first subdivion of the base not that divides the current tick
    while crt_tick < ticks_in_sequence:
        divisor = ticks_in_base_note
        while divisor > 0:
            if not crt_tick % divisor:
                ret = base_note * ticks_in_base_note / divisor
                if ret <= base_note * click_divide:
                    yield (ret, warn)
                else:
                    #silent note
                    yield None
            else:
                divisor /= 2
        crt_tick += 1

class TrackStream:
    def __init__(self, file, tick_note = 16):
        f = open(file, "r")
        self.track = json.load(f)
        self.__sequences = self.track["sequence"]

        # begin at sequnece 0 bar 0
        self.__sequences[0]["bars"]
        self.__crt_sequence_idx = 0
        self.__bar_idx = 0
        # create the generators for each sequence
        self.__tick_generators = [barnotes(bars[0], s["tempo"], s["click-divide"], tick_note, bars[1]) for s in self.__sequences \
            for bars in [(s["bars"] - s["warn"], False), (s["warn"], True)]]

    def advance(self):
        #return next 16th note
        # (BPM, note_to_play, warn)
        
        pass

    def getCurrent(self):
        #return (note (16th, 8th, 4th, first_in_bar), warn sequence end)
        pass

    