from pico2d import *
from PIL import Image

class UI_Black:
    image = None
    def __init__(self, _x, _y, _scaleX = 1, _scaleY = 1):
        self.x = _x
        self.y = _y
        self.scaleX = _scaleX
        self.scaleY = _scaleY

        if UI_Black.image == None:
            UI_Black.image = load_image('Resource/Texture/UI_Bar/Expbar_Black.png')
            SDL_SetTextureAlphaMod(UI_Black.image.texture, 150)

        self.sizeX = UI_Black.image.w * self.scaleX
        self.sizeY = UI_Black.image.h * self.scaleY

    def update(self):
        pass

    def draw(self):
        UI_Black.image.draw(self.x, self.y, self.sizeX, self.sizeY)