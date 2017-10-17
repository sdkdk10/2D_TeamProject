from pico2d import *
from transform import Transform as myTransform
#import player
from player import Player as myPlayer
from random import *

class Monster():
    def __init__(self, _player):
        global myTrans
        global Distance
        global player
        self.x = 300
        self.y = 300
        self.dirX = 0
        self.dirY = 0
        self.speed = 1
        self.image = load_image('Resource/Texture/new_Unit/Monster/Assassin.png')
        player = myPlayer()

    def draw(self):
        self.image.draw(self.posX(), self.posY())

    def update(self):
        self.dirX = player.getTransform().x - self.x
        self.dirY = player.getTransform().y - self.y
        Distance = math.sqrt(self.dirX * self.dirX + self.dirY * self.dirY)
        self.dirX /= Distance
        self.dirY /= Distance
        self.x += self.dirX * self.speed
        self.y += self.dirY * self.speed

    def setPos(self, x, y):
        self.x = x
        self.y = y

    def posX(self):
        return self.x

    def posY(self):
        return self.y

    def setDir(self, x, y):
        self.dirX = x
        self.dirY = y

    def setDirX(self, x):
        self.dirX = x

    def setDirY(self, y):
        self.dirY = y

    def dirX(self):
        return self.dirX

    def dirY(self):
        return self.dirY


