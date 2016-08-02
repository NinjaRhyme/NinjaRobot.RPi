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
        self.width = 640
        self.height = 480
        self.framerate = 24
        self.is_need_update = False
        self.luffing_signal = 7.5
        self.swing_signal = 7.5

    def __del__(self):
        pass

    # ----------------------------------------------------------------------------------------------------
    def process(self):
        if self.is_need_update:
            self.is_need_update = False
            self.luffing_signal_pin.ChangeDutyCycle(self.luffing_signal)
            self.swing_signal_pin.ChangeDutyCycle(self.swing_signal)

    # ----------------------------------------------------------------------------------------------------
    def getPinNames(self):
        return [
            "camera_luffing_steering_signal_pin",
            "camera_swing_steering_signal_pin",
        ];

    def setPins(self, pins):
        super(NinjaCamera, self).setPins(pins)
        luffing_signal_pin = self.pins["camera_luffing_steering_signal_pin"]
        swing_signal_pin = self.pins["camera_swing_steering_signal_pin"]
        try:
            GPIO.setup(luffing_signal_pin, GPIO.OUT)
            self.luffing_signal_pin = GPIO.PWM(luffing_signal_pin, 50)
            self.luffing_signal_pin.start(0)
            self.luffing_signal_pin.ChangeDutyCycle(self.luffing_signal)
            GPIO.setup(swing_signal_pin, GPIO.OUT)
            self.swing_signal_pin = GPIO.PWM(swing_signal_pin, 50)
            self.swing_signal_pin.start(0)
            self.swing_signal_pin.ChangeDutyCycle(self.swing_signal)
        except:
            pass

    # ----------------------------------------------------------------------------------------------------
    def onKeyInput(self, char):
        if char == 'i':
            if 6 < self.luffing_signal:
                self.luffing_signal -= 0.4
                if self.luffing_signal < 6:
                    self.luffing_signal = 6
            print("camera up", self.luffing_signal)
        elif char == 'k':
            if self.luffing_signal < 8:
                self.luffing_signal += 0.4
                if 8 < self.luffing_signal:
                    self.luffing_signal = 8
            print("camera down", self.luffing_signal)
        elif char == 'l':
            if 6 < self.swing_signal:
                self.swing_signal -= 0.4
                if self.swing_signal < 6:
                    self.swing_signal = 6
            print("camera left", self.swing_signal)
        elif char == 'j':
            if self.swing_signal < 8:
                self.swing_signal += 0.4
                if 8 < self.swing_signal:
                    self.swing_signal = 8
            print("camera right", self.swing_signal)
        else:
            return False
        self.is_need_update = True
        return True
