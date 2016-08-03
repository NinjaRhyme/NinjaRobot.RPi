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
        self.is_running = True
        self.robot = robot
        self.components = []
        self.init()

    # ----------------------------------------------------------------------------------------------------
    def process(self):
        while self.is_running:
            for component in self.components:
                component.process()
            time.sleep(0.1)
            pass
        self.exit()

    def stop(self):
        self.is_running = False

    def exit(self):
        try:
            for component in self.components:
                self.robot.controller.remove_observer(component)
                component.exit()
            self.components = []
            GPIO.cleanup()
        except:
            pass

    # ----------------------------------------------------------------------------------------------------
    def init(self):
        # GPIO
        try:
            GPIO.setwarnings(True)
            GPIO.setmode(GPIO.BCM)
        except:
            pass

        # components
        for name in self.robot.memory.config["components"]:
            module = __import__('NinjaComponent.' + name, globals(), locals(), [name])
            ComponentClass = getattr(module, name)
            self.components.append(ComponentClass(name))
        for component in self.components:
            self.robot.controller.add_observer(component)
            if "pins" in self.robot.memory.config["components"][component.name]:
                component.on_pins_connect(self.robot.memory.config["components"][component.name]["pins"])
