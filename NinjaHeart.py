# coding=utf-8

import time
try: # Debug
    import RPi.GPIO as GPIO
except:
    pass

# Test
from NinjaComponent.NinjaMotor import *

# ----------------------------------------------------------------------------------------------------
class NinjaHeart(object):
    def __init__(self, robot):
        self.robot = robot
        self.components = []
        self.initGPIO()
        self.initComponents()

    def __del__(self):
        try:
            for component in self.components:
                self.robot.controller.removeObserver(component)
            self.components = []
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
        for component in self.robot.memory.config["components"]:
            componentModule = __import__('NinjaComponent.' + component, globals(), locals(), [component])
            componentClass = getattr(componentModule, component)
            self.components.append(componentClass())

        for component in self.components:
            self.robot.controller.addObserver(component)
            pinNames = component.getPinNames()
            pins = {}
            for name in pinNames:
                if name in self.robot.memory.config:
                    pins[name] = self.robot.memory.config[name]
            component.setPins(pins)
