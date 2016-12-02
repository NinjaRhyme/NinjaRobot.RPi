# coding=utf-8

import time
import json

from NinjaObject import *

# ----------------------------------------------------------------------------------------------------
class NinjaMemory(NinjaObject):
    def __init__(self, robot):
        super(NinjaMemory, self).__init__()
        self.robot = robot

        self.config = {
            # components
            "components" : {
                "NinjaSteering" : {
                    "pins" : {
                        "car_steering_signal_pin" : 16
                    }
                },
                "NinjaMotor" : {
                    "pins" : {
                        "car_motor_forward_signal_pin" : 1,
                        "car_motor_backward_signal_pin" : 12
                    }
                },
                "NinjaCamera" : {
                    "pins" : {
                        "camera_luffing_steering_signal_pin" : 26,
                        "camera_swing_steering_signal_pin" : 13
                    },
                    "source_for_controller" : True
                }
            },
            # services
            "services" : {
                "NinjaWebService" : {
                    "port" : 8080,
                    "source_for_controller" : True
                }
            }
        }
        self.load_config()

    # ----------------------------------------------------------------------------------------------------
    def process(self):
        time.sleep(3)

    # ----------------------------------------------------------------------------------------------------
    def load_config(self):
        try:
            with open("Data/config.json", 'r') as fin:
                config = json.load(fin)
                self.config.update(config)
        except Exception as e:
            print("ERROR", e)
