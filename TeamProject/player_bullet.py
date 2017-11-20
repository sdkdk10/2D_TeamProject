from transform import Transform as myTransform
from pico2d import *

class Player_Bullet:
    image = None
    def __init__(self, _posX, _posY, _dirX, _dirY):
        self.myTrans = myTransform()
        self.myTrans.setPos(_posX, _posY)
        distance = _dirX * _dirX + _dirY * _dirY
        dirX = _dirX / distance
        dirY = _dirY / distance
        self.myTrans.setDir(dirX, dirY)
        self.myTrans.setSpeed(10)
        if Player_Bullet.image == None:
            self.image = load_image('Resource/Texture/Bullet/Basic.png')

    def update(self):
        self.myTrans.update()

    def draw(self):
        self.image.draw(self.myTrans.posX(), self.myTrans.posY(), 30, 30)