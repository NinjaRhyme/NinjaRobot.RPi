# coding=utf-8

import time

# ----------------------------------------------------------------------------------------------------
class NinjaMemory(object):
    def __init__(self, robot):
        self.is_running = True
        self.robot = robot
        self.config = {
            # components
            "components" : {
                "NinjaSteering" : {
                    "pins" : {
                        "car_steering_signal_pin" : 16,
                    },
                },
                "NinjaMotor" : {
                    "pins" : {
                        "car_motor_forward_signal_pin" : 1,
                        "car_motor_backward_signal_pin" : 12,
                    },
                },
                "NinjaCamera" : {
                    "pins" : {
                        "camera_luffing_steering_signal_pin" : 26,
                        "camera_swing_steering_signal_pin" : 13,
                    },
                },
            },
            # services
            "services" : {

            }
        }
        self.load_config()

    # ----------------------------------------------------------------------------------------------------
    def process(self):
        while self.is_running:
            time.sleep(0.1)
            pass
        self.exit()

    def stop(self):
        self.is_running = False

    def exit(self):
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
