# coding=utf-8

from Utility.NinjaGetch import NinjaGetch

# ----------------------------------------------------------------------------------------------------
class NinjaController(object):
    def __init__(self, robot):
        self.isRunning = True
        self.robot = robot
        self.getch = NinjaGetch();
        self.observers = [];

    # ----------------------------------------------------------------------------------------------------
    def process(self):
        while self.isRunning:
            char = self.getch()
            print("input", char)
            for observer in self.observers:
                if observer is not None and hasattr(observer, 'onKeyInput') and hasattr(observer.onKeyInput, '__call__'):
                    result = observer.onKeyInput(char)
                    if result:
                        break
            pass
        self.exit()

    def stop(self):
        self.isRunning = False

    def exit(self):
        self.observers = []

    # ----------------------------------------------------------------------------------------------------
    def addObserver(self, observer):
        if observer is not None:
            self.observers.append(observer)

    def removeObserver(self, observer):
        if observer is not None:
            self.observers.remove(observer)

    # ----------------------------------------------------------------------------------------------------
