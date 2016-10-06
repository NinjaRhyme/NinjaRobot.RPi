# coding=utf-8

import threading

# ----------------------------------------------------------------------------------------------------
class NinjaObject(object):
    def __init__(self):
        # state
        self.is_running = True
        self.thread = threading.Thread(target=self.run)
        self.thread.setDaemon(True)
        # observer
        self.observers = []
        pass

    # ----------------------------------------------------------------------------------------------------
    def start(self): # async
        self.thread.start()

    def join(self): # async -> sync
        self.thread.join()

    def run(self): # sync
        while self.is_running:
            self.process()
        self.exit()

    def process(self): # once
        pass

    def stop(self): # (async & sync) -> stop
        self.is_running = False

    def exit(self): # callback
        pass

    # ----------------------------------------------------------------------------------------------------
    def add_observer(self, observer):
        if observer is not None:
            self.observers.append(observer)

    def remove_observer(self, observer):
        if observer is not None:
            self.observers.remove(observer)

    def clear_observer(self):
        self.observers = []
