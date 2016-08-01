# coding=utf-8

try:
    import RPi.GPIO as GPIO
except:
    pass

from NinjaComponent import *

# ----------------------------------------------------------------------------------------------------
class NinjaLaser(NinjaComponent):
    def __init__(self):
        super(NinjaLaser, self).__init__()
        self.signal_pin = None
        self.is_need_update = False
        self.signal = 0

    def __del__(self):
        if self.signal_pin is not None:
            self.signal_pin.stop()

    # ----------------------------------------------------------------------------------------------------
    def process(self):
        if self.is_need_update:
            self.is_need_update = False
            self.signal_pin.ChangeDutyCycle(self.signal)

    # ----------------------------------------------------------------------------------------------------
    def getPinNames(self):
        return ["laser_signal_pin"];

    def setPins(self, pins):
        super(NinjaLaser, self).setPins(pins)
        signal_pin = self.pins["laser_signal_pin"]
        try:
            GPIO.setup(signal_pin, GPIO.OUT)
            self.signal_pin = GPIO.PWM(signal_pin, 50)
            self.signal_pin.start(0)
            self.signal_pin.ChangeDutyCycle(0)
        except:
            pass

    # ----------------------------------------------------------------------------------------------------
    def onKeyInput(self, char):
        if char == 'q':
            if 50 < self.signal:
                self.signal = 0
                print("laser off", self.signal)
            else:
                self.signal = 100
                print("laser on", self.signal)
        else:
            return False
        self.is_need_update = True
        return True