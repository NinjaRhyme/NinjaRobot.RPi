# coding=utf-8

import tornado.web

# ----------------------------------------------------------------------------------------------------
class BaseHandler(tornado.web.RequestHandler):

    # ----------------------------------------------------------------------------------------------------
    def initialize(self):
        if not self.get_secure_cookie("user_ip"):
            self.set_secure_cookie("user_ip", self.request.remote_ip)
        pass

    def data_received(self, chunk):
        pass

    def on_finish(self):
        pass

    def get(self):
        pass
