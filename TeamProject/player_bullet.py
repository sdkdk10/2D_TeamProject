from transform import Transform as myTransform
from pico2d import *

class Player_Bullet:
    image = None
    stack = None
    def __init__(self, _posX, _posY, _dirX, _dirY):
        global myTrans
        myTrans = myTransform()
        myTrans.setPos(_posX, _posY)
        distance = _dirX * _dirX + _dirY * _dirY
        dirX = _dirX / distance
        dirY = _dirY / distance
        myTrans.setDir(dirX, dirY)
        myTrans.setSpeed(10)
        if Player_Bullet.image == None:
            self.image = load_image('Resource/Texture/Bullet/Basic.png')

    def update(self):
        myTrans.update()
        for i in range(Player_Bullet.stack):
            Player_Bullet.stack[i]

    def draw(self):
        self.image.draw(myTrans.posX(), myTrans.posY())