# coding=utf-8

import sys
import json
import tornado.websocket

# ----------------------------------------------------------------------------------------------------
class InputHandler(tornado.websocket.WebSocketHandler):
    clients = []

    # ----------------------------------------------------------------------------------------------------
    def initialize(self, server):
        self.server = server

    def open(self):
        InputHandler.clients.append(self)
        self.set_nodelay(True)
        pass

    def data_received(self, chunk):
        pass

    def on_message(self, message):
        data = json.loads(message)
        if data is not None and self.server is not None:
            self.server.on_input_handle_event(data)

    def on_close(self):
        InputHandler.clients.remove(self)
