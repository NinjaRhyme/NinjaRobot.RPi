# coding=utf-8

import time

# ----------------------------------------------------------------------------------------------------
class NinjaMemory(object):
    def __init__(self, robot):
        self.robot = robot
        self.config = {
            # pins
            'car_steering_signal_pin' : 12,
            'car_left_motor_signal_pin' : 0,
            'car_right_motor_signal_pin' : 0,
        }
        self.load_config()

    # ----------------------------------------------------------------------------------------------------
    def process(self):
        while True:
            time.sleep(0.1)
            pass

    # ----------------------------------------------------------------------------------------------------
    def load_config(self):
        try:
            with open("Data/config", 'r') as fin:
                lines = fin.readlines()
                for line in lines:
                    words = line.split()
                    if self.config.has_key(words[0]) and isinstance(self.config[words[0]], int):
                        self.config[words[0]] = int(words[1])
                    else:
                        self.config[words[0]] = words[1]
        except Exception as e:
            print("ERROR", e)
