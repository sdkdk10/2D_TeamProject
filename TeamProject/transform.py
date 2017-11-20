from pico2d import *

class Transform:
    def __init__(self):
        #global x, y
        self.x = 0
        self.y = 0
        self.dirX = 0
        self.dirY = 0
        self.speed = 1
        self.sizeX = 0
        self.sizeY = 0

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

    def getDirX(self):
        return self.dirX

    def getDirY(self):
        return self.dirY

    def setSpeed(self, _speed):
        self.speed = _speed

    def setSize(self, _x, _y):
        self.sizeX = _x
        self.sizeY = _y

    def sizeX(self):
        return self.sizeX

    def sizeY(self):
        return self.sizeY