from pico2d import *
from transform import Transform as myTransform
import collision

class Monster_Bullet:
    image = None
    def __init__(self, _x, _y, _dirX, _dirY, _player):
        global player
        self.myTrans = myTransform()
        self.myTrans.setPos(_x, _y)
        distance = _dirX * _dirX + _dirY * _dirY
        dirX = _dirX / distance
        dirY = _dirY / distance
        self.myTrans.setDir(dirX, dirY)
        self.myTrans.setSpeed(10)
        self.myTrans.setSize(25, 25)
        self.count = 0
        player = _player
        self.isDead = False
        if Monster_Bullet.image == None:
            self.image = load_image('Resource/Texture/Bullet/MonsterBullet.png')


    def draw(self):
        self.image.draw(self.myTrans.posX(), self.myTrans.posY(), 25, 25)

    def update(self):
        global player
        self.myTrans.update()
        self.count += 1
        if self.count > 70:
            self.isDead = True
        if player != None:
            pass
        if collision.collision_distance_A(self, player) == True:
            self.isDead = True
            player.isDead = True
            print("player Col")

    def getIsDead(self):
        return self.isDead

    def colX(self):
        return self.myTrans.posX()

    def colY(self):
        return self.myTrans.posY()


    def getTransform(self):
        return self.myTrans