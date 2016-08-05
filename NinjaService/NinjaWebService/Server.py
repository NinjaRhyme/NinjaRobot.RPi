# coding=utf-8

import os
import base64
import uuid
import time
import tornado.ioloop
import tornado.web
import tornado.httputil
import tornado.autoreload
import threading

from NinjaObject import *
from .Handler.IndexHandler import IndexHandler
from .Handler.InputHandler import InputHandler

# ----------------------------------------------------------------------------------------------------
class Server(NinjaObject):
    def __init__(self, name):
        super(Server, self).__init__()
        self.name = name

        print(os.system("webpack --config " + os.path.join(os.path.dirname(__file__), "webpack.config.js")))
        self.port = 8080
        self.application = tornado.web.Application(
            [
                (r"/", IndexHandler),
                (r"/input", InputHandler, dict(server=self)),
                (r"/(.*)", tornado.web.StaticFileHandler, dict(path=os.path.join(os.path.dirname(__file__), "Static"))),
            ],
            template_path=os.path.join(os.path.dirname(__file__), "Template"),
            cookie_secret=base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes),
            login_url=r"/", # Todo
        )
        self.observers = []

    # ----------------------------------------------------------------------------------------------------
    def run(self):
        self.application.listen(self.port)
        tornado.ioloop.IOLoop.instance().start() # current
        self.exit()

    def process(self): # Trick, running in the other thread
        pass

    def stop(self):
        tornado.ioloop.IOLoop.instance().stop()

    def exit(self):
        self.clear_observer()

    # ----------------------------------------------------------------------------------------------------
    def add_observer(self, observer):
        if observer is not None:
            self.observers.append(observer)

    def remove_observer(self, observer):
        if observer is not None:
            self.observers.remove(observer)

    def clear_observer(self):
        self.observers = []

    # ----------------------------------------------------------------------------------------------------
    def on_configure(self, data):
        if "port" in data:
            self.port = data["port"]

    # ----------------------------------------------------------------------------------------------------
    def on_input_handle_event(self, data):
        if "key" in data:
            key = data["key"]
            print("input", key)
            for observer in self.observers:
                if observer is not None and hasattr(observer, 'on_web_key_input') and hasattr(observer.on_web_key_input, '__call__'):
                    result = observer.on_web_key_input(key)
                    if result:
                        break
