# coding=utf-8

import time

# ----------------------------------------------------------------------------------------------------
class NinjaMemory(object):
    def __init__(self, robot):
        self.robot = robot
        self.config = {
            # components
            "components" : [
                "NinjaSteering",
                "NinjaMotor",
            ],
            # pins
            "car_steering_signal_pin" : 16,
            "car_motor_forward_signal_pin" : 1,
            "car_motor_backward_signal_pin" : 12,
        }
        self.load_config()

    # ----------------------------------------------------------------------------------------------------
    def process(self):
        while True:
            time.sleep(0.1)
            pass

    # Todo
    # ----------------------------------------------------------------------------------------------------
    def load_config(self):
        try:
            with open("Data/config", 'r') as fin:
                lines = fin.readlines()
                for line in lines:
                    words = line.split()
                    if words[0] in self.config and isinstance(self.config[words[0]], int):
                        self.config[words[0]] = int(words[1])
                    else:
                        self.config[words[0]] = words[1]
        except Exception as e:
            print("ERROR", e)
