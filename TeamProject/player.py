from pico2d import *
from transform import Transform as myTransform

#myTransform = None

class Player:
    def __init__(self):
        #global myTransform
        global myTrans
        self.image = load_image('Resource/Texture/Unit/Base.png')
        myTrans = myTransform()
        myTrans.setPos(600, 386)
    def draw(self):
        self.image.rotate_draw(math.radians(90), myTrans.posX(), myTrans.posY())

    def update(self):
        myTrans.update()

    def handle_events(self, event):
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_w:
                myTrans.setDirY(1)
            elif event.key == SDLK_s:
                myTrans.setDirY(-1)
            elif event.key == SDLK_a:
                myTrans.setDirX(-1)
            elif event.key == SDLK_d:
                myTrans.setDirX(1)

        if event.type == SDL_KEYUP:
            if event.key == SDLK_w:
                myTrans.setDirY(0)
            elif event.key == SDLK_s:
                myTrans.setDirY(0)
            elif event.key == SDLK_a:
                myTrans.setDirX(0)
            elif event.key == SDLK_d:
                myTrans.setDirX(0)


    def getTransform(self):
        return myTrans
