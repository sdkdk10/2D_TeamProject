from pico2d import *
from transform import Transform as myTransform
#import player
from player import Player as myPlayer
from Monster import Monster as myMonster
from monster_bullet import Monster_Bullet as myBullet
#from random import *
import background
import random
import collision

class Boss():
    def __init__(self,_bg, _player):
        global Distance
        global player
        global bg
        global bulletStack
        global update_bullet
        bulletStack = None
        update_bullet = None
        player = _player
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
        self.shootTime = 0
        self.isShooting = False
        self.bulletAngle = 0
        #player = _player
        bg = _bg
        #---------------별그리기에 필요한것들

    def draw(self):
        global update_bullet
        if update_bullet != None:
            stacklen = len(update_bullet)
            for i in range(stacklen):
                update_bullet[i].draw()
        # self.image.draw(self.posX(), self.posY())
        self.scrollX = self.myTrans.posX() - bg.window_left
        self.scrollY = self.myTrans.posY() - bg.window_bottom
        self.image.rotate_draw(math.radians(self.angle), self.scrollX, self.scrollY)
        #self.image.draw(self.scrollX, self.scrollY)


    def shootBullet(self):
        global bulletStack
        dirX = math.cos(math.radians(self.bulletAngle))
        dirY = math.sin(math.radians(self.bulletAngle))
        posX = self.myTrans.posX() + (dirX * 20)
        posY = self.myTrans.posY() + (dirY * 20)
        newbull = myBullet(posX, posY, dirX, dirY)
        self.bulletAngle += 36
        if self.bulletAngle >= 360:
            self.isShooting = False
            self.bulletAngle = 0

        if bulletStack == None:
            bulletStack = [newbull]
        else:
            bulletStack.append(newbull)
        pass

    def update(self):
        global bulletStack, update_bullet, player
        self.angle += 5
        self.myTrans.update()
        self.scrollX = self.myTrans.posX() - bg.window_left
        self.scrollY = self.myTrans.posY() - bg.window_bottom

        if self.isShooting == False:
            self.shootTime += 1
            if self.shootTime > 50:
                self.shootTime = 0
                self.isShooting = True
                print("boss shooting=======================))")
        else:
            bulletdirX = math.cos(math.radians(self.bulletAngle))
            bulletdirY = math.sin(math.radians(self.bulletAngle))
            posX = self.scrollX + (bulletdirX * 20)
            posY = self.scrollY + (bulletdirY * 20)
            newbull = myBullet(posX, posY, bulletdirX, bulletdirY, player)
            self.bulletAngle += 36
            if self.bulletAngle >= 360:
                self.isShooting = False
                self.bulletAngle = 0

            if bulletStack == None:
                bulletStack = [newbull]
            else:
                bulletStack.append(newbull)

        if bulletStack != None:
            update_bullet = [b for b in bulletStack if b.getIsDead() == False]

        if update_bullet != None:
            stacklen = len(update_bullet)
            for i in range(stacklen):
                update_bullet[i].update()




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