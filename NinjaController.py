# coding=utf-8

from NinjaObject import *
from Utility.NinjaGetch import NinjaGetch

# event: on_key_input (Todo, keyboard controller -> Heart)
# ----------------------------------------------------------------------------------------------------
class NinjaController(NinjaObject):
    def __init__(self, robot):
        super(NinjaController, self).__init__()
        self.robot = robot

        self.getch = NinjaGetch()
        self.sources = []
        self.observers = []

    # ----------------------------------------------------------------------------------------------------
    def process(self):
        char = self.getch()
        print("input", char)
        for observer in self.observers:
            if observer is not None and hasattr(observer, 'on_key_input') and hasattr(observer.on_key_input, '__call__'):
                result = observer.on_key_input(char)
                if result:
                    break
        pass

    def exit(self):
        self.clear_observer()

    # ----------------------------------------------------------------------------------------------------
    def add_source(self, source):
        if source is not None:
            self.sources.append(source)
            for observer in self.observers:
                source.add_observer(observer)

    def remove_source(self, source):
        if source is not None:
            self.sources.remove(source)
            source.clear_observer()

    def clear_source(self):
        self.sources = []

    def add_observer(self, observer):
        if observer is not None:
            self.observers.append(observer)
            for source in self.sources:
                source.add_observer(observer)

    def remove_observer(self, observer):
        if observer is not None:
            self.observers.remove(observer)
            for source in self.sources:
                source.remove_observer(observer)

    def clear_observer(self):
        self.observers = []

    # ----------------------------------------------------------------------------------------------------
