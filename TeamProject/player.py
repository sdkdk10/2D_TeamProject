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
        myTrans.setPos(600, 386)
        myTrans.setSpeed(2)
        #myTrans.setSize(self.image.w, self.image.h)
        self.angle = 0
        self.angleDir = 0

    def draw(self):
        self.image.rotate_draw(math.radians(self.angle), myTrans.posX(), myTrans.posY())

    def update(self):
        global mouseX, mouseY
        myTrans.update()
        self.angle += self.angleDir
        if self.angle > 360:
            self.angle -= 360
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
                newBull = myBullet(myTrans.posX(), myTrans.posY(), math.cos(math.radians(self.angle)), math.sin(math.radians(self.angle)))
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
        return myTrans