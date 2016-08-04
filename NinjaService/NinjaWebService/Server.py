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

try:
    from .Handler.IndexHandler import IndexHandler
except:
    from Handler.IndexHandler import IndexHandler

# ----------------------------------------------------------------------------------------------------
class Server(object):
    def __init__(self, name):
        self.name = name
        self.port = 8080
        self.application = tornado.web.Application(
            [
                (r"/", IndexHandler),
                (r"/(.*)", tornado.web.StaticFileHandler, dict(path=os.path.join(os.path.dirname(__file__), "Static"))),
            ],
            template_path=os.path.join(os.path.dirname(__file__), "Template"),
            cookie_secret=base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes),
            login_url=r"/", # Todo
        )

    # ----------------------------------------------------------------------------------------------------
    def start(self):
        pass

    def run(self):
        self.application.listen(self.port)
        tornado.ioloop.IOLoop.instance().start() # current
        self.exit()

    def process(self):
        pass

    def stop(self):
        tornado.ioloop.IOLoop.instance().stop()

    def exit(self):
        pass
