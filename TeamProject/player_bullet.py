from transform import Transform as myTransform
from pico2d import *
import collision
import player_bullet_mgr

class Player_Bullet:
    image = None
    monster = None
    global player
    player = None
    def __init__(self, _posX, _posY, _dirX, _dirY, _player):
        global player
        self.myTrans = myTransform()
        self.myTrans.setPos(_posX, _posY)
        distance = _dirX * _dirX + _dirY * _dirY
        dirX = _dirX / distance
        dirY = _dirY / distance
        self.myTrans.setDir(dirX, dirY)
        self.myTrans.setSpeed(10)
        self.myTrans.setSize(25, 25)
        if player == None:
            player = _player
        if Player_Bullet.image == None:
            self.image = load_image('Resource/Texture/Bullet/Basic.png')

        self.count = 0

    def update(self):
        self.myTrans.update()
        #if Player_Bullet.monster != None:
        #    if collision.collision_distance(self.myTrans, Player_Bullet.monster.getTransform()) == True:
        #        print("Collision!!")

        stacklen = len(player_bullet_mgr.expMonster)
        for i in range(stacklen):
            mon = player_bullet_mgr.expMonster[i]
            if collision.collision_distance(self.myTrans.posX(), self.myTrans.posY(), self.myTrans.sizeX, mon.getScrollX(), mon.getScrollY(), mon.getTransform().sizeX) == True:
                print("Collision")
                return 1

        self.count += 1
        #print(self.count)
        if self.count > 50:
            return 1

        return 0

    def draw(self):
        self.image.draw(self.myTrans.posX(), self.myTrans.posY(), 25, 25)

    def getTransform(self):
        return self.myTrans

    def setMonster(self, monster):
        if Player_Bullet.monster == None:
            Player_Bullet.monster = monster