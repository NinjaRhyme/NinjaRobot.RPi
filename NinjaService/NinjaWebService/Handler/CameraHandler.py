# coding=utf-8

import sys
import json
import tornado.websocket

# ----------------------------------------------------------------------------------------------------
class CameraHandler(tornado.websocket.WebSocketHandler):
    clients = []

    # ----------------------------------------------------------------------------------------------------
    def initialize(self, server):
        self.server = server

    def open(self):
        if self.server is not None:
            self.write_message(self.server.on_camera_handle_connect_event(), binary=True)
        CameraHandler.clients.append(self)
        self.set_nodelay(True)
        pass

    def data_received(self, chunk):
        pass

    def on_message(self, message):
        pass

    def on_close(self):
        CameraHandler.clients.remove(self)

    # ----------------------------------------------------------------------------------------------------
    @staticmethod
    def broadcast(buf):
        for client in CameraHandler.clients:
            client.write_message(buf, binary=True)
        pass
