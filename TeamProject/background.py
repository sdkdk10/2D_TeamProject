from pico2d import *

class Background:
    def __init__(self):
        self.image = load_image('Resource/Texture/BG/BG.png')
        self.x = 600
        self.y = 386
    def draw(self):
        self.image.draw(self.x, self.y)
