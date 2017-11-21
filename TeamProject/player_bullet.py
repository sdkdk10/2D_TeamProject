from transform import Transform as myTransform
from pico2d import *
import collision

class Player_Bullet:
    image = None
    monster = None
    def __init__(self, _posX, _posY, _dirX, _dirY):
        self.myTrans = myTransform()
        self.myTrans.setPos(_posX, _posY)
        distance = _dirX * _dirX + _dirY * _dirY
        dirX = _dirX / distance
        dirY = _dirY / distance
        self.myTrans.setDir(dirX, dirY)
        self.myTrans.setSpeed(10)
        self.myTrans.setSize(25, 25)
        if Player_Bullet.image == None:
            self.image = load_image('Resource/Texture/Bullet/Basic.png')

    def update(self):
        self.myTrans.update()
        if Player_Bullet.monster != None:
            if collision.collision_distance(self.myTrans, Player_Bullet.monster.getTransform()) == True:
                print("Collision!!")

    def draw(self):
        self.image.draw(self.myTrans.posX(), self.myTrans.posY(), 25, 25)

    def getTransform(self):
        return self.myTrans

    def setMonster(self, monster):
        if Player_Bullet.monster == None:
            Player_Bullet.monster = monster