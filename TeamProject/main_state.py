import game_framework
import title_state
import player_bullet_mgr

from player import Player as myPlayer
from background import Background as myBackground
from Monster import Monster as myMonster
from ExpBox import ExpBox as myExpBox

from pico2d import *

name = "TitleState"
image = None

def enter():
    global player
    player = myPlayer()
    global team
    team = [myMonster(player) for i in range(10)]
    global background
    background = myBackground()
    global Monster
    Monster = myMonster(player)
    global ExpBox
    ExpBox = myExpBox(player)
    global team1
    team1 = [myExpBox(player) for i in range(500)]
    player_bullet_mgr.enter(Monster)


def exit():
    global background
    del(background)
    global player
    del(player)
    global Monster
    del(Monster)
    global ExpBox
    del(ExpBox)
    global team
    del team
    global team1
    del team1
    player_bullet_mgr.exit()

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
    global player
    player.update()
    for monster_team in team:
        monster_team.update()
    for expBox_team in team1:
        expBox_team.update()
    player_bullet_mgr.update()

def draw():
    global player
    clear_canvas()
    background.draw()
    for monster_team in team:
        monster_team.draw()
    for expBox_team in team1:
        expBox_team.draw()

    player_bullet_mgr.draw()
    player.draw()
    update_canvas()
