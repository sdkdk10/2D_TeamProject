from pico2d import *

class Transform:
    def __init__(self):
        global x, y
        self.x = 0
        self.y = 0

    def translate(self, x, y):
        self.x += x
        self.y += y