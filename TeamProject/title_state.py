import game_framework
import main_state
from pico2d import *

name = "TitleState"
image = None

def enter():
    global image
    open_canvas(1200, 772,  0)
    image = load_image('Resource/Texture/BG/title.png')
    #change_windowpos(200, 200)

def exit():
    global image
    del(image)

def update():
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(main_state)

def draw():
    clear_canvas()
    image.draw(600, 386)
    update_canvas()