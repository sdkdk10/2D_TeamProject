from pico2d import *
from transform import Transform as myTransform
from random import *
import random

class ExpBox:
    def __init__(self, _player):
        global state
        global background
        state = random.randint(1,3)
        self.myTrans = myTransform()
        self.myTrans.setPos(random.randint(0, 5000), random.randint(100, 5000))
        self.myTrans.setDir(1, 1)
        self.myTrans.setSpeed(0.005)
        self.x = 300
        self.y = 300
        self.dirX = 1
        self.dirY = 1
        self.speed = 1
        self.scrollX = 0
        self.scrollY = 0
        if (state == 1):
            self.image = load_image('Resource/Texture/new_Unit/EXP_BOX/Pentagon1.png')
        elif(state == 2):
            self.image = load_image('Resource/Texture/new_Unit/EXP_BOX/Triangle1.png')
        elif(state == 3):
            self.image = load_image('Resource/Texture/new_Unit/EXP_BOX/Rectangle1.png')

        self.myTrans.setSize(self.image.w, self.image.h)

    def set_background(self, _bg):
        global background
        background = _bg
    def draw(self):
        global background
        sx = self.myTrans.posX() - background.window_left
        sy = self.myTrans.posY() - background.window_bottom
        self.scrollX = sx
        self.scrollY = sy
        #self.image.draw(self.myTrans.posX(), self.myTrans.posY())
        self.image.draw(sx, sy)

    def update(self):
        self.myTrans.setDir(random.randint(1,3), random.randint(1,3))
        self.myTrans.update()
        self.x += self.dirX * self.speed
        self.y += self.dirY * self.speed

    def getTransform(self):
        return self.myTrans

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

    def dirX(self):
        return self.dirX

    def dirY(self):
        return self.dirY

    def getScrollX(self):
        return self.scrollX

    def getScrollY(self):
        return self.scrollY


    def getTransform(self):
        return self.myTrans


