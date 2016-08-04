# coding=utf-8

try:
    import RPi.GPIO as GPIO
except:
    pass

from .NinjaComponent import *

# ----------------------------------------------------------------------------------------------------
class NinjaLaser(NinjaComponent):
    def __init__(self, name):
        super(NinjaLaser, self).__init__(name)
        self.signal_pin = None
        self.is_need_update = False
        self.signal = 0

    # ----------------------------------------------------------------------------------------------------
    def process(self):
        if self.is_need_update:
            self.is_need_update = False
            self.signal_pin.ChangeDutyCycle(self.signal)

    def exit(self):
        if self.signal_pin is not None:
            self.signal_pin.stop()

    # ----------------------------------------------------------------------------------------------------
    def on_pins_connect(self, pins):
        super(NinjaLaser, self).on_pins_connect(pins)
        signal_pin = self.pins["laser_signal_pin"]
        try:
            GPIO.setup(signal_pin, GPIO.OUT)
            self.signal_pin = GPIO.PWM(signal_pin, 50)
            self.signal_pin.start(0)
            self.signal_pin.ChangeDutyCycle(self.signal)
        except:
            pass

    # ----------------------------------------------------------------------------------------------------
    def on_key_input(self, char):
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
