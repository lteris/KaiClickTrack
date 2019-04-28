''' Load configuration from json input file '''

import json

'''click_divide = division of the base note that is not silent; =2 on tempo */4 means play every 8th note
   tick_note = frequency of the pulse - tick_note=16 => every 16th note you get called
   barcount = number of bars in this sequnce

   Return - the type of note to play for every tick_note: 4th, 8th ... or None if the note
   on the current tick is silent. 
'''
def barnotes(barcount, tempo="4/4", click_divide=1, tick_note = 16, warn = False):
    tempo_supra, base_note = tempo_split(tempo)

    #number of ticks in the whole sequence
    ticks_in_bar = (int)(tempo_supra / base_note * tick_note)
    ticks_in_base_note = (int)(tick_note / base_note)

    for bar in range(barcount):
        first_in_bar = True

        # find the first subdivion of the base note that divides the current tick
        for crt_tick  in range(ticks_in_bar):
            divisor = ticks_in_base_note
            while divisor > 0:
                if not crt_tick % divisor:
                    ret = base_note * ticks_in_base_note / divisor
                    if ret > base_note * click_divide:
                        ret = None
                    
                    #set divisor to 0 to break out of the while loop
                    divisor = 0
                    yield (ret, first_in_bar, warn)
                    
                else:
                    divisor /= 2
            
            first_in_bar = False
    return

def tempo_split(tempo):
    return list(map(int, tempo.split("/")))


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
        self.__tick_generators = [(s["bpm"], tempo_split(s["tempo"])[1] ,barnotes(bars[0], s["tempo"], s["click-divide"], tick_note, bars[1])) for s in self.__sequences \
            for bars in [(s["bars"] - s["warn"], False), (s["warn"], True)]]

    def nextNote(self):
        #return next 16th note
        # (BPM, note_to_play, warn)
        crt_tick = self.__tick_generators[self.__crt_sequence_idx]
        
        while True:
            try:
                bpm = crt_tick[0]
                base_note = crt_tick[1]
                note = next(crt_tick[2])
                yield (bpm, base_note, note)
            except StopIteration:
                #move to next sequence
                if self.__crt_sequence_idx < len(self.__tick_generators) - 1:
                    self.__crt_sequence_idx += 1
                    crt_tick = self.__tick_generators[self.__crt_sequence_idx]
                else:
                    return