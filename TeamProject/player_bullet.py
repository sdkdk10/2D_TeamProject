from transform import Transform as myTransform
from pico2d import *

class Player_Bullet:
    image = None
    def __init__(self, _posX, _posY, _dirX, _dirY):
        global myTrans
        myTrans = myTransform()
        myTrans.setPos(_posX, _posY)
        myTrans.setDir(_dirX, _dirY)
        if Player_Bullet.image == None:
            self.image = load_image('Resource/Texture/Bullet/Basic.png')

    def Update(self):
        myTrans.update()

    def draw(self):
        self.image.draw(myTrans.posX(), myTrans.posY())