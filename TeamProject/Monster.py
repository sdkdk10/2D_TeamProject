from pico2d import *
from transform import Transform as myTransform
#import player
from player import Player as myPlayer
from ExpBox import ExpBox as expbox
#from random import *
import background
import random
from enum import Enum
import math
import player_bullet_mgr
import collision

class Monsterstate(Enum):
    monster_left = 1
    monster_right = 2
    monster_top = 3
    monster_bottom = 4
    monster_leftup = 5
    monster_rightup = 6
    monster_leftdown = 7
    monster_rightdown = 8

class Monster():
    def __init__(self, _player, _bg):
        global Distance
        global player
        global bg

        self.myTrans = myTransform()
        self.myTrans.setPos(random.randint(100, 5000), random.randint(100, 5000))
        self.myTrans.setDir(1, 0)
        self.myTrans.setSpeed(0)
        self.x = 0
        self.y = 0
        self.dirX = 1
        self.dirY = 0
        self.lookX = 1
        self.lookY = 0
        self.speed = 0
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
        self.fcos = 0
        self.isDead_sound = load_wav('monsterdie.wav')

        #=============================몬스터 state
        self.state = 0

    def draw(self):
        self.scrollX = self.myTrans.posX() - bg.window_left
        self.scrollY = self.myTrans.posY() - bg.window_bottom
        self.image.rotate_draw(math.radians(self.angle), self.scrollX, self.scrollY)

    def update(self):
        self.myTrans.setDir(self.dirX, self.dirY)
        self.myTrans.update()
        self.scrollX = self.myTrans.posX() - bg.window_left
        self.scrollY = self.myTrans.posY() - bg.window_bottom
        self.dirX = player.getScrollX() - self.scrollX
        self.dirY = player.getScrollY() - self.scrollY
        Distance = math.sqrt(self.dirX * self.dirX + self.dirY * self.dirY)
        Distance2 = math.sqrt(self.lookX * self.lookX + self.lookY * self.lookY)
        if Distance == 0:
            self.dirY = 0
            self.dirX = 0
        else :
            self.dirX /= Distance
            self.dirY /= Distance
        if Distance2 == 0:
            self.lookX = 0
            self.lookY = 0
        else :
            self.lookX /= Distance2
            self.lookY /= Distance2

        #============================================ 몬스터가 플레이어 보는거 범위 설정 추가해야됨
        self.fcos = self.lookX * self.dirX + self.lookY * self.dirY
        self.angle = math.degrees(math.acos(self.fcos))

        if (self.dirY < self.lookY):
            self.angle = 360 - self.angle
        self.scrollX += math.cos(self.angle * math.pi) * 5
        self.scrollY += math.sin(self.angle * math.pi) * 5
        self.myTrans.setSpeed(1.5)

        #============================== 몬스터 스크롤
        if self.scrollX > 5000:
            --self.scrollX
        elif self.scrollX <= 0:
            ++self.scrollX
        elif self.scrollY > 5000:
            --self.scrollY
        elif self.scrollY <= 0:
            ++self.scrollY

        #=================몬스터끼리 충돌처리
        stacklen = len(player_bullet_mgr.monster)
        for i in range(stacklen):
            mon = player_bullet_mgr.monster[i]
            if collision.collision_distance_A(self,mon) == True:
                print("collision")
                return True
        #====================사운드



    def getTransform(self):
        return self.myTrans

    def boundingbox(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

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
        if self.isDead_sound == None:
            self.isDead_sound = load_wav('monsterdie.wav')
            self.isDead_sound.set_volume(32)
            self.isDead()

    def isDead(self):
        self.isDead_sound.play()

    def getIsDead(self):
        return self.isDead

    def monstermove(self):
        self.state = random.randint(1, 9)
        if (self.temp > 100):
            if self.state == Monsterstate.monster_left:
                self.scrollX -= 1
                self.angle = 180
                self.myTrans.setSpeed(1)
            elif self.state == Monsterstate.monster_right:
                self.scrollX += 1
                self.angle = 0
                self.myTrans.setSpeed(1)
            elif self.state == Monsterstate.monster_top:
                self.scrollY -= 1
                self.angle = 90
                self.myTrans.setSpeed(1)
            elif self.state == Monsterstate.monster_bottom:
                self.scrollY += 1
                self.angle = 360
                self.myTrans.setSpeed(1)
            elif self.state == Monsterstate.monster_leftup:
                self.scrollX -= 1
                self.scrollY -= 1
                self.myTrans.setSpeed(1)
            elif self.state == Monsterstate.monster_leftdown:
                self.scrollX -= 1
                self.scrollY += 1
                self.myTrans.setSpeed(1)
            elif self.state == Monsterstate.monster_rightup:
                self.scrollX += 1
                self.scrollY -= 1
                self.myTrans.setSpeed(1)
            elif self.state == Monsterstate.monster_rightdown:
                self.scrollX += 1
                self.scrollY += 1
                self.myTrans.setSpeed(1)