from pico2d import *
from transform import Transform as myTransform
#import player
from player import Player as myPlayer
from random import *

class Monster():
    def __init__(self, _player):
        global Distance
        global player
        #-----------------By. JH----------------------
        self.myTrans = myTransform()
        self.myTrans.setPos(300, 300)
        self.myTrans.setDir(0, 0)
        self.myTrans.setSpeed(1)

        self.x = 300
        self.y = 300
        self.dirX = 0
        self.dirY = 0
        self.speed = 1
        self.angle = 0
        self.angleDir = 0
        self.image = load_image('Resource/Texture/new_Unit/Monster/Assassin.png')
        #self.myTrans.setSize(self.image.w, self.image.h)`
        player = myPlayer()

    def draw(self):
        #self.image.draw(self.posX(), self.posY())
        self.image.draw(self.myTrans.posX(), self.myTrans.posY())

    def update(self):
        #self.dirX = player.getTransform().x - self.x
        #self.dirY = player.getTransform().y - self.y

        self.dirX = player.getTransform().x - self.myTrans.posX()
        self.dirY = player.getTransform().y - self.myTrans.posY()
        Distance = math.sqrt(self.dirX * self.dirX + self.dirY * self.dirY)
        self.dirX /= Distance
        self.dirY /= Distance
        self.myTrans.setDir(self.dirX, self.dirY)
        self.myTrans.update()
        #self.x += self.dirX * self.speed
        #self.y += self.dirY * self.speed

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


