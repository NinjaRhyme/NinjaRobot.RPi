# coding=utf-8

from NinjaObject import *

# ----------------------------------------------------------------------------------------------------
class NinjaComponent(NinjaObject):
    def __init__(self, name):
        self.name = name
        self.pins = {}
        pass

    # ----------------------------------------------------------------------------------------------------
    def on_configure(self, data):
        if "pins" in data:
            self.pins.update(data["pins"])

    # ----------------------------------------------------------------------------------------------------
    def on_key_input(self, char):
        return False
