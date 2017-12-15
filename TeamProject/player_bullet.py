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
        self.isDead = False
        if player == None:
            player = _player
        if Player_Bullet.image == None:
            self.image = load_image('Resource/Texture/Bullet/Basic.png')

        self.count = 0

    def update(self):
        global player
        self.myTrans.update()

        stacklen = len(player_bullet_mgr.expMonster)
        for i in range(stacklen):
            expmon = player_bullet_mgr.expMonster[i]
            if collision.collision_distance_A(self, expmon) == True:
                #print("Collision")
                self.isDead = True
                expmon.isDead = True
                player.setExp(5)
                return 1

        stacklen_mon = len(player_bullet_mgr.monster)
        for i in range(stacklen_mon):
            mon = player_bullet_mgr.monster[i]
            if collision.collision_distance_A(self, mon) == True:
                #print("Monster Collision")
                self.isDead = True
                mon.setIsDead(True)

                player.setExp(10)
                return 1

        self.count += 1
        #print(self.count)
        if self.count > player.range:
            self.isDead = True
            return 1

        self.isDead = False
        return 0

    def draw(self):
        self.image.draw(self.myTrans.posX(), self.myTrans.posY(), 25, 25)

    def getTransform(self):
        return self.myTrans

    def setMonster(self, monster):
        if Player_Bullet.monster == None:
            Player_Bullet.monster = monster

    def setIsDead(self, bDead):
        self.isDead = bDead

    def getIsDead(self):
        return self.isDead

    def colX(self):
        return self.myTrans.posX()

    def colY(self):
        return self.myTrans.posY()

    def IsCol(self, iscol):
        self.isDead = iscol