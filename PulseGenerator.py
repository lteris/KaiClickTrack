''' Generate a tick and drive the sound and graphics engine '''
import time

class PulseGenerator:
    def __init__(self, stream):
        self.stream = stream
        self.subscribers = []

    def addSubscriber(self, subscribers):
        self.subscribers.extend(subscribers)
    
    #generate tick on every 16th note at the current BPM
    def run(self):
        noteGenerator = self.stream.advance()
        for nextNote in noteGenerator:
            (bpm, (note, isEnd)) = nextNote 
            
            for sub in self.subscribers:
                sub.doTick()
            #time.sleep(0.01)