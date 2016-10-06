# coding=utf-8

import sys
import io
import os
import time
try:
    import RPi.GPIO as GPIO
    import picamera
except:
    pass

from struct import Struct
from subprocess import Popen, PIPE
from .NinjaComponent import *

# event: on_camera_output
# ----------------------------------------------------------------------------------------------------
class NinjaCamera(NinjaComponent):
    def __init__(self, name):
        super(NinjaCamera, self).__init__(name)
        # steering
        self.is_need_update = False
        self.luffing_signal = 7.5
        self.swing_signal = 7.5
        # camera
        self.width = 640
        self.height = 480
        self.framerate = 24
        self.JSMPEG_MAGIC = b'jsmp'
        self.JSMPEG_HEADER = Struct('>4sHH')
        self.camera = picamera.PiCamera()
        self.camera.resolution = (self.width, self.height)
        self.camera.framerate = self.framerate
        time.sleep(1) # camera warm-up time
        self.output = CameraOutput(self.camera)
        self.camera.start_recording(self.output, 'yuv') # record

    # ----------------------------------------------------------------------------------------------------
    def process(self):
        # steering
        if self.is_need_update:
            self.is_need_update = False
            self.luffing_signal_pin.ChangeDutyCycle(self.luffing_signal)
            self.swing_signal_pin.ChangeDutyCycle(self.swing_signal)
        # camera
        self.camera.wait_recording(1)
        buf = self.output.converter.stdout.read(512)
        if buf:
            for observer in self.observers:
                if observer is not None and hasattr(observer, 'on_camera_output') and hasattr(observer.on_camera_output, '__call__'):
                    result = observer.on_camera_output(buf)
            pass
        elif self.converter.poll() is not None:
            pass

    # ----------------------------------------------------------------------------------------------------
    def on_configure(self, data):
        super(NinjaCamera, self).on_configure(data)
        luffing_signal_pin = self.pins["camera_luffing_steering_signal_pin"]
        swing_signal_pin = self.pins["camera_swing_steering_signal_pin"]
        try:
            GPIO.setup(luffing_signal_pin, GPIO.OUT)
            self.luffing_signal_pin = GPIO.PWM(luffing_signal_pin, 50)
            self.luffing_signal_pin.start(0)
            self.luffing_signal_pin.ChangeDutyCycle(self.luffing_signal)
            GPIO.setup(swing_signal_pin, GPIO.OUT)
            self.swing_signal_pin = GPIO.PWM(swing_signal_pin, 50)
            self.swing_signal_pin.start(0)
            self.swing_signal_pin.ChangeDutyCycle(self.swing_signal)
        except:
            pass

    # ----------------------------------------------------------------------------------------------------
    def on_key_input(self, char):
        if char == 'i':
            if 6 < self.luffing_signal:
                self.luffing_signal -= 0.4
                if self.luffing_signal < 6:
                    self.luffing_signal = 6
            print("camera up", self.luffing_signal)
        elif char == 'k':
            if self.luffing_signal < 8:
                self.luffing_signal += 0.4
                if 8 < self.luffing_signal:
                    self.luffing_signal = 8
            print("camera down", self.luffing_signal)
        elif char == 'l':
            if 6 < self.swing_signal:
                self.swing_signal -= 0.4
                if self.swing_signal < 6:
                    self.swing_signal = 6
            print("camera left", self.swing_signal)
        elif char == 'j':
            if self.swing_signal < 8:
                self.swing_signal += 0.4
                if 8 < self.swing_signal:
                    self.swing_signal = 8
            print("camera right", self.swing_signal)
        else:
            return False
        self.is_need_update = True
        return True

    def on_web_camera_connect(self):
        return self.JSMPEG_HEADER.pack(self.JSMPEG_MAGIC, self.width, self.height)

# ----------------------------------------------------------------------------------------------------
class CameraOutput(object):
    def __init__(self, camera):
        print('Spawning background conversion process')
        self.converter = Popen([
            'avconv',
            '-f', 'rawvideo',
            '-pix_fmt', 'yuv420p',
            '-s', '%dx%d' % camera.resolution,
            '-r', str(float(camera.framerate)),
            '-i', '-',
            '-f', 'mpeg1video',
            '-b', '800k',
            '-r', str(float(camera.framerate)),
            '-'],
            stdin=PIPE, stdout=PIPE, stderr=io.open(os.devnull, 'wb'),
            shell=False, close_fds=True)

    def write(self, b):
        self.converter.stdin.write(b)

    def flush(self):
        print('Waiting for background conversion process to exit')
        self.converter.stdin.close()
        self.converter.wait()
