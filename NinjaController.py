# coding=utf-8

from Utility.NinjaGetch import NinjaGetch

# ----------------------------------------------------------------------------------------------------
class NinjaController(object):
    def __init__(self, robot):
        self.is_running = True
        self.robot = robot
        self.getch = NinjaGetch();
        self.observers = [];

    # ----------------------------------------------------------------------------------------------------
    def process(self):
        while self.is_running:
            char = self.getch()
            print("input", char)
            for observer in self.observers:
                if observer is not None and hasattr(observer, 'on_key_input') and hasattr(observer.on_key_input, '__call__'):
                    result = observer.on_key_input(char)
                    if result:
                        break
            pass
        self.exit()

    def stop(self):
        self.is_running = False

    def exit(self):
        self.observers = []

    # ----------------------------------------------------------------------------------------------------
    def add_observer(self, observer):
        if observer is not None:
            self.observers.append(observer)

    def remove_observer(self, observer):
        if observer is not None:
            self.observers.remove(observer)

    # ----------------------------------------------------------------------------------------------------
