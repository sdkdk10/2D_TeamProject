from pico2d import *
from transform import Transform as myTransform
#import player
from player import Player as myPlayer
from Monster import Monster as myMonster
#from random import *
import background
import random
import collision

class Boss():
    def __init__(self,_bg):
        global Distance
        global player
        global bg

        self.myTrans = myTransform()
        self.myTrans.setPos(2500, 2500)
        self.myTrans.setDir(0, 0)
        self.myTrans.setSpeed(0)
        self.x = 300
        self.y = 300
        self.dirX = 0
        self.dirY = 0
        self.speed = 0
        self.scrollX = 0
        self.scrollY = 0
        self.angle = 0
        self.isDead = False
        self.image = load_image('Resource/Texture/new_Unit/Monster/Boss/OctoTank.png')
        self.myTrans.setSize(self.image.w, self.image.h)
        #player = _player
        bg = _bg
        #---------------별그리기에 필요한것들

    def draw(self):
        # self.image.draw(self.posX(), self.posY())
        self.scrollX = self.myTrans.posX() - bg.window_left
        self.scrollY = self.myTrans.posY() - bg.window_bottom
        self.image.rotate_draw(math.radians(self.angle), self.scrollX, self.scrollY)
        #self.image.draw(self.scrollX, self.scrollY)

    def update(self):
        self.angle += 5
        self.myTrans.update()
        self.scrollX = self.myTrans.posX() - bg.window_left
        self.scrollY = self.myTrans.posY() - bg.window_bottom

    #def tanmak(self):

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