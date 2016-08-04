# coding=utf-8

from .BaseHandler import *

class IndexHandler(BaseHandler):
    def get(self):
        self.render("index.html")
