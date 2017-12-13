from pico2d import *

class UI_Num:
    image = None
    def __init__(self, _x, _y, _scale = 1):
        self.x = _x
        self.y = _y
        self.scale = _scale
        self.score = 0
        route = 'Resource/Texture/UI_Font/Num/'
        if UI_Num.image == None:
            for i in range(10):
                num = str(i)
                fullRoute = route + num + '.png'
                if i == 0:
                    UI_Num.image = [load_image(route + num + '.png')]
                else:
                    UI_Num.image.append(load_image(route + num + '.png'))

        self.sizeX = UI_Num.image[0].w * self.scale
        self.sizeY = UI_Num.image[0].h * self.scale

    def draw(self):
        cnt = 0
        for i in range(2, -1, -1):
            if (self.score / pow(10, i)) > 0:
                cnt = i + 1
                break

        drawScore = self.score
        drawX = self.x
        drawY = self.y
        for i in range(cnt):
            texNum = int(drawScore / (pow(10, cnt - 1 - i)))
            drawScore = drawScore % (pow(10, cnt - 1 - i))
            UI_Num.image[texNum].draw(drawX, drawY, self.sizeX, self.sizeY)
            drawX += (UI_Num.image[texNum].w / 2 + (7 * self.scale))

    def setScore(self, _score):
        self.score = _score
