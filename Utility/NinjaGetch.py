# coding=utf-8

# ----------------------------------------------------------------------------------------------------
class NinjaGetch:
    def __init__(self):
        try:
            self.impl = NinjaGetchWindows()
        except ImportError:
            self.impl = NinjaGetchUnix()

    def __call__(self):
        return self.impl()


class NinjaGetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class NinjaGetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()
