# coding=utf-8

try:
    import RPi.GPIO as GPIO
except:
    pass

from NinjaComponent import *

# ----------------------------------------------------------------------------------------------------
class NinjaCamera(NinjaComponent):
    def __init__(self):
        super(NinjaCamera, self).__init__()

    def __del__(self):
        pass

    # ----------------------------------------------------------------------------------------------------
    def process(self):
        pass

    # ----------------------------------------------------------------------------------------------------
    def getPinNames(self):
        return [""];

    def setPins(self, pins):
        super(NinjaCamera, self).setPins(pins)

    # ----------------------------------------------------------------------------------------------------
    def onKeyInput(self, char):
        return False
