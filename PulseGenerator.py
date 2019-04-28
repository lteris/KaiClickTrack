''' Generate a tick and drive the sound and graphics engine '''
import time

class PulseGenerator:
    def __init__(self, stream):
        self._stream = stream
        self._subscribers = []

    def addSubscriber(self, subscribers):
        self._subscribers.extend(subscribers)
    
    #generate tick on every 16th note at the current BPM
    def run(self):
        noteGenerator = self._stream.nextNote()
        for nextNote in noteGenerator:
            (bpm, base_note, (note, isFirstInBar, isEnd)) = nextNote 

            if note != None:
                print(str(bpm) + " " + str(base_note) + " ")
 
            for sub in self._subscribers:
                sub.doTick(note, isFirstInBar, isEnd)

            # Play <bpm> base notes per minute. Get the sleep time in seconds between 2 16th notes.
            sleep_time = 60 / (bpm * 16 / base_note)
            time.sleep(sleep_time)