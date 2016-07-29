# coding=utf-8

import time
try: # Debug
    import RPi.GPIO as GPIO
except:
    pass

# Test
from NinjaComponent.NinjaSteering import *

# ----------------------------------------------------------------------------------------------------
class NinjaHeart(object):
    def __init__(self, robot):
        self.robot = robot
        self.components = []
        self.initGPIO()
        self.initComponents()

    def __del__(self):
        try:
            GPIO.cleanup()
        except:
            pass

    # ----------------------------------------------------------------------------------------------------
    def process(self):
        while True:
            for component in self.components:
                component.process()
            time.sleep(0.1)
            pass

    # ----------------------------------------------------------------------------------------------------
    def initGPIO(self):
        try:
            GPIO.setwarnings(True)
            GPIO.setmode(GPIO.BCM)
        except:
            pass

    # ----------------------------------------------------------------------------------------------------
    def initComponents(self):
        steering = NinjaSteering()
        self.robot.controller.addObserver(steering)
        self.components.append(steering)

        for component in self.components:
            pinNames = component.getPinNames()
            pins = {}
            for name in pinNames:
                if self.robot.memory.config.has_key(name):
                    pins[name] = self.robot.memory.config[name]
            component.setPins(pins)
