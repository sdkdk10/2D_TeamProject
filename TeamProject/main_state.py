import game_framework
import title_state

from player import Player as myPlayer
from background import Background as myBackground
from Monster import Monster as myMonster
from pico2d import *

name = "TitleState"
image = None

def enter():
    global player
    player = myPlayer()
    global background
    background = myBackground()
    global monster
    monster = myMonster()

def exit():
    global background
    del(background)
    global player
    del(player)
    del(monster)

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        else:
            player.handle_events(event)

def update():
    player.update()
    #monster.update()


def draw():
    clear_canvas()
    background.draw()
    player.draw()
    #monster.draw()
    update_canvas()
