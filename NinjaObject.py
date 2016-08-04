# coding=utf-8

import threading

# ----------------------------------------------------------------------------------------------------
class NinjaObject(object):
    def __init__(self):
        self.is_running = True
        self.thread = threading.Thread(target=self.run)
        self.thread.setDaemon(True)
        pass

    # ----------------------------------------------------------------------------------------------------
    def start(self):
        self.thread.start()

    def join(self):
        self.thread.join()

    def run(self):
        while self.is_running:
            self.process()
        self.exit()

    def process(self):
        pass

    def stop(self):
        self.is_running = False

    def exit(self):
        pass
