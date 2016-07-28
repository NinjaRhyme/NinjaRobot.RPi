# coding=utf-8

import Utility.NinjaGetch as NinjaGetch

# ----------------------------------------------------------------------------------------------------
class NinjaController(object):
    def __init__(self, robot):
        self.robot = robot
        self.getch = NinjaGetch();
        self.observers = [];

    # ----------------------------------------------------------------------------------------------------
    def process(self):
        while True:
            time.sleep(0.1)
            pass

    # ----------------------------------------------------------------------------------------------------
    def addObserver(self, observer):
        pass

    def removeObserver(self, observer):
        pass

    # ----------------------------------------------------------------------------------------------------
