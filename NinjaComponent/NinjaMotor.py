# coding=utf-8

from NinjaComponent import *

# ----------------------------------------------------------------------------------------------------
class NinjaMotor(NinjaComponent):
    def __init__(self):
        super(NinjaMotor, self).__init__()
        pass

    # ----------------------------------------------------------------------------------------------------
    def process(self):
        pass

    # ----------------------------------------------------------------------------------------------------
    def getPinNames(self):
        return ["car_left_motor_forward_signal_pin",
            "car_left_motor_backward_signal_pin",
            "car_right_motor_forward_signal_pin",
            "car_right_motor_backward_signal_pin"];

    # ----------------------------------------------------------------------------------------------------
    def onKeyInput(self, char):
        if char == 'w':
            print("forward")
            return True
        elif char == 's':
            print("backward")
            return True
        return False
