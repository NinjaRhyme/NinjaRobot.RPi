import threading

from NinjaMemory import *
from NinjaHeart import *

# ----------------------------------------------------------------------------------------------------
class NinjaRobot(object):
    def __init__(self):
        self.memory = NinjaMemory(self)
        self.memory_thread = threading.Thread(target=self.memory.process)
        self.memory_thread.setDaemon(True)
        self.heart = NinjaHeart(self)
        self.heart_thread = threading.Thread(target=self.heart.process)
        self.heart_thread.setDaemon(True)
        pass

    # ----------------------------------------------------------------------------------------------------
    def run(self):
        self.memory_thread.start()
        self.heart_thread.start()
        try:
            while 1:
                time.sleep(0.1)
        except KeyboardInterrupt:
            self.exit()

    # ----------------------------------------------------------------------------------------------------
    def exit(self):
        # Do something
        print("exit")
