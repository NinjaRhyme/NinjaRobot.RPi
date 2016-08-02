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
        self.isRunning = True
        self.robot = robot
        self.components = []
        self.initGPIO()
        self.initComponents()

    # ----------------------------------------------------------------------------------------------------
    def process(self):
        while self.isRunning:
            for component in self.components:
                component.process()
            time.sleep(0.1)
            pass
        self.exit()

    def stop(self):
        self.isRunning = False

    def exit(self):
        try:
            for component in self.components:
                self.robot.controller.removeObserver(component)
                component.exit()
            self.components = []
            GPIO.cleanup()
        except:
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
