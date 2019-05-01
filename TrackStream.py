''' Load configuration from json input file '''

import json

''' Type of sound to use in a bar
'''
class BarTickSound:
    NORMAL = 0
    WARN = 1
    PAUSE = 2

''' Information about a sequence and the corresponding note generator
'''
class SequenceInfo:
    def __init__(self, bpm, tempo, comment, barcount, click_divide, tick_note, tick_sound):
        self._bpm = bpm
        self._upper_note, self._base_note = tempo_split(tempo)
        self._comment = comment
        self._bar_notes = barnotes(barcount, tempo, click_divide, tick_note, tick_sound)



'''click_divide = division of the base note that is not silent; =2 on tempo */4 means play every 8th note
   tick_note = frequency of the pulse - tick_note=16 => every 16th note you get called
   barcount = number of bars in this sequnce

   Return - the type of note to play for every tick_note: 4th, 8th ... or None if the note
   on the current tick is silent. 
'''
def barnotes(barcount, tempo="4/4", click_divide=1, tick_note = 16, warn = BarTickSound.NORMAL):
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
        self.__crt_sequence_idx = 0

        # create the generators for each sequence
        self.__tick_generators = [SequenceInfo(s["bpm"], s["tempo"], s.get("comment", " "), bars[0], s["click-divide"], tick_note, bars[1]) \
            for s in self.__sequences \
            for bars in [(s["bars"], BarTickSound.NORMAL), (s.get("warn", 0), BarTickSound.WARN), (s.get("pause", 0), BarTickSound.PAUSE)] ]

    def nextNote(self):
        #return next 16th note
        # (BPM, note_to_play, warn)
        seq_info = self.__tick_generators[self.__crt_sequence_idx]
        
        while True:
            try:
                note = next(seq_info._bar_notes)
                yield (seq_info._bpm, seq_info._base_note, note)
            except StopIteration:
                #move to next sequence
                if self.__crt_sequence_idx < len(self.__tick_generators) - 1:
                    self.__crt_sequence_idx += 1
                    seq_info = self.__tick_generators[self.__crt_sequence_idx]
                    print(">>>>>>>>>>>>>>>>>>>> " + seq_info._comment + " <<<<<<<<<<<<<<<<<<<<<<<<<")
                else:
                    return