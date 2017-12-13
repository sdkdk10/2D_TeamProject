from pico2d import *
from transform import Transform as myTransform
#import player
from player import Player as myPlayer
#from random import *
import background
import random

class Monster():
    def __init__(self, _player, _bg):
        global Distance
        global player
        global bg
        #-----------------By. JH----------------------
        self.myTrans = myTransform()
        self.myTrans.setPos(random.randint(100, 5000), random.randint(100, 5000))
        self.myTrans.setDir(0, 0)
        self.myTrans.setSpeed(1)

        self.x = 300
        self.y = 300
        self.dirX = 0
        self.dirY = 0
        self.speed = 1
        self.angle = 0
        self.angleDir = 0
        self.scrollX = 0
        self.scrollY = 0
        self.isDead = False
        self.image = load_image('Resource/Texture/new_Unit/Monster/Assassin.png')
        self.myTrans.setSize(self.image.w, self.image.h)
        #player = myPlayer()
        player = _player
        bg = _bg


    def draw(self):
        self.image.draw(self.scrollX, self.scrollY)

    def update(self):
        #self.dirX = player.getTransform().x - self.x
        #self.dirY = player.getTransform().y - self.y

        #self.dirX = player.getScrollX() - self.myTrans.posX()
        #self.dirY = player.getScrollY() - self.myTrans.posY()
        self.dirX = player.getScrollX() - self.scrollX
        self.dirY = player.getScrollY() - self.scrollY
        Distance = math.sqrt(self.dirX * self.dirX + self.dirY * self.dirY)
        if Distance == 0:
            self.dirY = 0
            self.dirX = 0
        else :
            self.dirX /= Distance
            self.dirY /= Distance
        self.myTrans.setDir(self.dirX, self.dirY)
        self.myTrans.update()
        self.scrollX = self.myTrans.posX() - bg.window_left
        self.scrollY = self.myTrans.posY() - bg.window_bottom
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

    def getScrollX(self):
        return self.scrollX

    def getScrollY(self):
        return self.scrollY

    def isInWindow(self):
        if self.scrollX > 0 and self.scrollX < get_canvas_width():
            if self.scrollY > 0 and self.scrollY < get_canvas_height():
                return True
        return False

    def colX(self):
        return self.scrollX

    def colY(self):
        return self.scrollY

    def setIsDead(self, bDead):
        self.isDead = bDead

    def getIsDead(self):
        return self.isDead