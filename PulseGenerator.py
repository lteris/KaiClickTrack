''' Generate a tick and drive the sound and graphics engine '''

class PulseGenerator:
    def __init__(self, stream):
        self.stream = stream
        self.subscribers = []

    def addSubscriber(self, subscribers):
        self.subscribers.append(subscribers)
    
    def run():
        while True:
            #generate tick on every 16th note at the current BPM
            pass

            for sub in self.subscribers:
                sub.doTick()