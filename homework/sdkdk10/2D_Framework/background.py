from pico2d import *

class Background:
    SCROLL_SPEED_PPS = 200
    image = None
    def __init__(self):
        if Background.image == None:
            Background.image = load_image('background.png')
        self.x = 480
        self.left = 0
        self.speed = 0
        self.screen_width = 960
        self.screen_height = 272
        pass

    def draw(self):
        x = int(self.left)
        w = min(Background.image.w - x, self.screen_width)
        Background.image.clip_draw_to_origin(x, 0, w, self.screen_height, 0, 0)
        Background.image.clip_draw_to_origin(0, 0, self.screen_width - w, self.screen_height, w, 0)

    def update(self, frame_time):
        self.left = (self.left + frame_time * self.speed) % self.image.w

    def handle_event(self, event):
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_LEFT:
                self.speed -= Background.SCROLL_SPEED_PPS
            elif event.key == SDLK_RIGHT:
                self.speed += Background.SCROLL_SPEED_PPS
        if event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT:
                self.speed += Background.SCROLL_SPEED_PPS
            elif event.key == SDLK_RIGHT:
                self.speed -= Background.SCROLL_SPEED_PPS
