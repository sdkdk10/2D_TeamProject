from pico2d import *

class UI_Font:
    def __init__(self, _x, _y, _imageroute):
        self.x = _x
        self.y = _y
        self.image = load_image(_imageroute)

    def draw(self):
        self.image.draw(self.x, self.y)