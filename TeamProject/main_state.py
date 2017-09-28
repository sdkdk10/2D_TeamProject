import game_framework
import title_state
from pico2d import *

name = "TitleState"
image = None

class Background:
    def __init__(self):
        self.image = load_image('Resource/Texture/BG/BG.png')

    def draw(self):
        self.image.draw(600, 386)

def enter():
    global background
    background = Background()

def exit():
    global background
    del(background)

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)

def update():
    pass

def draw():
    clear_canvas()
    background.draw()
    update_canvas()