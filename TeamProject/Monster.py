from pico2d import *
from transform import Transform as myTransform
import player

class Monster:
    def __init__(self):
        global myTrans
        global Distance
        self.image = load_image('Resource/Texture/new_Unit/Monster/Assassin.png')
        myTrans = myTransform()
        myTrans.setPos(400, 386)

    def draw(self):
        self.image.draw(myTrans.posX(), myTrans.posY())

    def update(self):
        myTrans.update()

        myTransform.dirX =  - myTransform.x
        myTransform.diry =  - myTransform.y
        Distance = math.sqrt(myTransform.dirX * myTransform.dirX + myTransform.dirY * myTransform.dirY)

        myTransform.dirX /= Distance
        myTransform.dirY /= Distance

        myTransform.x += myTransform.dirX * 3
        myTransform.y += myTransform.dirY * 3

