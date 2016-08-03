# coding=utf-8

import threading

from NinjaController import *
from NinjaMemory import *
from NinjaHeart import *

# ----------------------------------------------------------------------------------------------------
class NinjaRobot(object):
    def __init__(self):
        self.is_running = True
        self.controller = NinjaController(self)
        self.controller_thread = threading.Thread(target=self.controller.process)
        self.controller_thread.setDaemon(True)
        self.memory = NinjaMemory(self)
        self.memory_thread = threading.Thread(target=self.memory.process)
        self.memory_thread.setDaemon(True)
        self.heart = NinjaHeart(self)
        self.heart_thread = threading.Thread(target=self.heart.process)
        self.heart_thread.setDaemon(True)

        self.controller.add_observer(self)
        pass

    # ----------------------------------------------------------------------------------------------------
    def run(self):
        self.controller_thread.start()
        self.memory_thread.start()
        self.heart_thread.start()
        while self.is_running:
            time.sleep(1)
            pass
        self.exit()

    def stop(self):
        self.is_running = False

    def exit(self):
        self.heart.stop()
        self.heart_thread.join()
        self.memory.stop()
        self.memory_thread.join()
        self.controller.stop()
        self.controller_thread.join()
        print("exit")

    # ----------------------------------------------------------------------------------------------------
    def on_key_input(self, char):
        if char == '\x03':
            self.stop()
            return True
        return False
