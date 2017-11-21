from pico2d import *

class Background:
    def __init__(self):
        self.image = load_image('Resource/Texture/BG/BG.png')
        self.x = 600
        self.y = 386
        self.center_object = None
        self.window_left = 0
        self.window_bottom = 0
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h

    def draw(self):
        #self.image.draw(self.x, self.y)
        self.image.clip_draw_to_origin(self.window_left, self.window_bottom, self.canvas_width, self.canvas_height, 0,0)

    def update(self):
        objectTrans = self.center_object.getTransform()
        objectPosX = objectTrans.posX()
        objectPosY = objectTrans.posY()
        self.window_left = clamp(0, int(objectPosX) - self.canvas_width // 2, self.w - self.canvas_width)
        self.window_bottom = clamp(0, int(objectPosY) - self.canvas_height // 2, self.h - self.canvas_height)
        #self.window_left = int(objectPosX) - self.canvas_width // 2
        #self.window_bottom = int(objectPosY) - self.canvas_height // 2
        print('BackGround : window_left = %d, window_bottom = %d' % (self.window_left, self.window_bottom))

    def set_center_object(self, _object):
        self.center_object = _object
