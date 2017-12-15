from pico2d import *

class UI_Value:
    def __init__(self, _x, _y, _maxScore, _route, _object, _scaleX = 1, _scaleY = 1):
        self.x = _x
        self.y = _y
        self.image = load_image(_route)
        self.scaleX = _scaleX
        self.scaleY = _scaleY
        self.sizeX = self.image.w * self.scaleX
        self.sizeY = self.image.h * self.scaleY
        self.curScore = 0
        self.maxScore = _maxScore
        self.level = 1
        self.object = _object

    def draw(self):
        #self.image.draw(self.x, self.y, self.sizeX, self.sizeY)
        percent = (self.curScore / self.maxScore)
        imagePercent = percent * self.image.w
        left = imagePercent / 2
        startX = self.x - self.sizeX / 2
        drawSizeX = min(int(left) * self.scaleX, self.sizeX)
        self.image.clip_draw_to_origin(0, 0, int(left), self.image.h, startX, self.y - self.sizeY / 2, drawSizeX, self.sizeY)
        self.image.clip_draw_to_origin(self.image.w - int(left), 0, self.image.w, self.image.h, startX + drawSizeX - 1, self.y - self.sizeY / 2, int(left) * self.scaleX, self.sizeY)

    def SetCurScore(self, _score):
        self.curScore += _score
        if self.curScore > self.maxScore:
            self.curScore = 0
            self.level += 1
            self.object.ValueUIlevel(self.level)
        elif self.curScore < 0:
            print("------------------Level minus---------------")
            --self.level

    def getCurScore(self):
        return self.curScore
