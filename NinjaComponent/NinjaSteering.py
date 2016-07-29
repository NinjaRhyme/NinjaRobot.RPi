# coding=utf-8

from NinjaComponent import *

# ----------------------------------------------------------------------------------------------------
class NinjaSteering(NinjaComponent):
    def __init__(self):
        super(NinjaSteering, self).__init__()
        pass

    # ----------------------------------------------------------------------------------------------------
    def process(self):
        pass

    # ----------------------------------------------------------------------------------------------------
    def getPinNames(self):
        return ["car_steering_signal_pin"];

    # ----------------------------------------------------------------------------------------------------
    def onKeyInput(self, char):
        if char == 'a':
            print("left")
            return True
        elif char == 'd':
            print("right")
            return True
        return False
