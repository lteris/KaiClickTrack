''' Generate a tick and drive the sound and graphics engine '''

class PulseGenerator:
    def __init__(self, stream):
        self.stream = stream
        self.subscribers = []

    def addSubscriber(self, subscribers):
        self.subscribers.extend(subscribers)
    
    def run(self):
        while True:
            #generate tick on every 16th note at the current BPM
            for sub in self.subscribers:
                sub.doTick()