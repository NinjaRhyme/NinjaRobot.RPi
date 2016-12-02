# coding=utf-8

from NinjaObject import *
from NinjaController import *
from NinjaMemory import *
from NinjaHeart import *

# ----------------------------------------------------------------------------------------------------
class NinjaRobot(NinjaObject):
    def __init__(self):
        super(NinjaRobot, self).__init__()

        self.controller = NinjaController(self)
        self.memory = NinjaMemory(self)
        self.heart = NinjaHeart(self)

        self.controller.add_observer(self)
        pass

    # ----------------------------------------------------------------------------------------------------
    def run(self):
        self.controller.start()
        #self.memory.start()
        self.heart.start()
        super(NinjaRobot, self).run()

    def process(self):
        self.heart.join()
        #time.sleep(3)

    def exit(self):
        self.heart.stop()
        self.heart.join()
        self.memory.stop()
        self.memory.join()
        self.controller.stop()
        self.controller.join()
        print("exit")

    # ----------------------------------------------------------------------------------------------------
    def on_key_input(self, char):
        if char == '\x03':
            self.stop()
            return True
        return False
