from pico2d import *
from transform import Transform as myTransform
from player_bullet import Player_Bullet as myBullet

import player_bullet_mgr

#myTransform = None

class Player:
    def __init__(self):
        global myTrans
        global mouseX, mouseY
        mouseX = 0
        mouseY = 0
        self.image = load_image('Resource/Texture/new_Unit/Player/1.png')
        myTrans = myTransform()
        myTrans.setPos(1000, 500)
        myTrans.setSpeed(2)
        myTrans.setSize(self.image.w, self.image.h)
        self.angle = 0
        self.angleDir = 0
        self.background = None
        self.scrollX = 0
        self.scrollY = 0

    def set_background(self, _background):
        self.background = _background

    def draw(self):
        global myTrans
        self.scrollX = myTrans.posX() - self.background.window_left
        self.scrollY = myTrans.posY() - self.background.window_bottom
        X = myTrans.posX()
        Y = myTrans.posY()
        self.image.rotate_draw(math.radians(self.angle), self.scrollX, self.scrollY)
        #print('Player : x = %d, y = %d' % (X, Y))
        #print('SX : %d sY : %d' % (self.scrollX, self.scrollY))


    def update(self):
        global myTrans
        self.angle += self.angleDir
        if self.angle > 360:
            self.angle -= 360
        myTrans.update()
        posX = clamp(0, myTrans.posX(), self.background.w)
        posY = clamp(0, myTrans.posY(), self.background.h)
        myTrans.setPos(posX, posY)
        #mouseToPlayerX = mouseX - myTrans.posX()
        #mouseToPlayerY = mouseY - myTrans.posY()
        #distance = mouseToPlayerX * mouseToPlayerX + mouseToPlayerY * mouseToPlayerY
        #mouseToPlayerX /= distance
        #mouseToPlayerY /= distance
#
        #dot = mouseToPlayerX * mouseToPlayerX + mouseToPlayerY * mouseToPlayerY
        #if dot != 0:
        #    self.angle = math.acos(dot)
        #if myTrans.posY() <= mouseY:
        #    self.angle = 360 - self.angle


    def handle_events(self, event):
        global myTrans
        global mouseX, mouseY
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_w:
                myTrans.setDirY(1)
            elif event.key == SDLK_s:
                myTrans.setDirY(-1)
            elif event.key == SDLK_a:
                myTrans.setDirX(-1)
            elif event.key == SDLK_d:
                myTrans.setDirX(1)
            elif event.key == SDLK_q:
                self.angleDir = 1
            elif event.key == SDLK_e:
                self.angleDir = -1
            elif event.key == SDLK_SPACE:
                #newBull = myBullet(myTrans.posX(), myTrans.posY(), math.cos(math.radians(self.angle)), math.sin(math.radians(self.angle)))
                newBull = myBullet(self.scrollX, self.scrollY, math.cos(math.radians(self.angle)),math.sin(math.radians(self.angle)), self)
                player_bullet_mgr.add_bullet(newBull)


        if event.type == SDL_KEYUP:
            if event.key == SDLK_w:
                myTrans.setDirY(0)
            elif event.key == SDLK_s:
                myTrans.setDirY(0)
            elif event.key == SDLK_a:
                myTrans.setDirX(0)
            elif event.key == SDLK_d:
                myTrans.setDirX(0)
            elif event.key == SDLK_q:
                self.angleDir = 0
            elif event.key == SDLK_e:
                self.angleDir = 0

        if event.type == SDL_MOUSEMOTION:
            mouseX, mouseY = event.x, 600 - event.y

    def getTransform(self):
        global myTrans
        return myTrans

    def getScrollX(self):
        return self.scrollX

    def getScrollY(self):
        return self.scrollY