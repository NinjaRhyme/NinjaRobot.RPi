# coding=utf-8

try:
    import RPi.GPIO as GPIO
except:
    pass

from .NinjaComponent import *

# ----------------------------------------------------------------------------------------------------
class NinjaSteering(NinjaComponent):
    def __init__(self):
        super(NinjaSteering, self).__init__()
        self.signal_pin = None
        self.is_need_update = False
        self.signal = 7.5

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
        return ["car_steering_signal_pin"];

    def setPins(self, pins):
        super(NinjaSteering, self).setPins(pins)
        signal_pin = self.pins["car_steering_signal_pin"]
        try:
            GPIO.setup(signal_pin, GPIO.OUT)
            self.signal_pin = GPIO.PWM(signal_pin, 50)
            self.signal_pin.start(0)
            self.signal_pin.ChangeDutyCycle(self.signal)
        except:
            pass

    # ----------------------------------------------------------------------------------------------------
    def onKeyInput(self, char):
        if char == 'a':
            if 6 < self.signal:
                self.signal -= 0.4
                if self.signal < 6:
                    self.signal = 6
            print("left", self.signal)
        elif char == 'd':
            if self.signal < 8:
                self.signal += 0.4
                if 8 < self.signal:
                    self.signal = 8
            print("right", self.signal)
        else:
            return False
        self.is_need_update = True
        return True
