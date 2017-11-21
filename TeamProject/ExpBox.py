from pico2d import *
from transform import Transform as myTransform
from random import *
import random

class ExpBox:
    def __init__(self, _player):
        global state
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
        if (state == 1):
            self.image = load_image('Resource/Texture/new_Unit/EXP_BOX/Pentagon1.png')
        elif(state == 2):
            self.image = load_image('Resource/Texture/new_Unit/EXP_BOX/Triangle1.png')
        elif(state == 3):
            self.image = load_image('Resource/Texture/new_Unit/EXP_BOX/Rectangle1.png')
    def draw(self):
        self.image.draw(self.myTrans.posX(), self.myTrans.posY())

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


