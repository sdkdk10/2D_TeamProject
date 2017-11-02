from pico2d import *
from transform import Transform as myTransform
from player_bullet import Player_Bullet as myBullet

#myTransform = None

class Player:
    def __init__(self):
        global myTrans
        global mouseX, mouseY
        global newBull
        newBull = None
        mouseX = 0
        mouseY = 0
        self.image = load_image('Resource/Texture/new_Unit/Player/1.png')
        myTrans = myTransform()
        myTrans.setPos(600, 386)
        myTrans.setSpeed(2)
        self.angle = 0
        self.angleDir = 0
    def draw(self):
        global newBull
        self.image.rotate_draw(math.radians(self.angle), myTrans.posX(), myTrans.posY())
        if newBull != None:
            newBull.draw()

    def update(self):
        global mouseX, mouseY, newBull
        myTrans.update()
        self.angle += self.angleDir
        if self.angle > 360:
            self.angle -= 360
        if newBull != None:
            newBull.update()
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
        global newBull
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
                i = 0


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