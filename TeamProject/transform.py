from pico2d import *

class Transform:
    def __init__(self):
        #global x, y
        self.x = 0
        self.y = 0
        self.dirX = 0
        self.dirY = 0
        self.speed = 5

    def translate(self, x, y):
        self.x += x
        self.y += y

    def update(self):
        self.x += self.dirX * self.speed
        self.y += self.dirY * self.speed

    def setPos(self, x, y):
        self.x = x
        self.y = y

    def posX(self):
        return self.x

    def posY(self):
        return self.y

    def setDir(self, x, y):
        self.dirX = x
        self.dirY = y

    def setDirX(self, x):
        self.dirX = x

    def setDirY(self, y):
        self.dirY = y