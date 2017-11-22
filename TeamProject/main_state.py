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
    global background
    background = myBackground()
    background.set_center_object(player)
    player.set_background(background)
    global team
    team = [myMonster(player, background) for i in range(100)]
    global Monster
    Monster = myMonster(player, background)
    player_bullet_mgr.enter(Monster)
    global team1
    team1 = [myExpBox(player) for i in range(500)]

    for i in team1:
        i.set_background(background)
        player_bullet_mgr.add_Monster(i)

def exit():
    global background
    del(background)
    global player
    del(player)
    global Monster
    del(Monster)
    player_bullet_mgr.exit()
    for i in range(team):
        del(team[i])
    for i in range(team1):
        del(team1[i])

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
    global player, background
    player.update()
    background.update()
    for monster_team in team:
        monster_team.update()
    for expBox_team in team1:
        expBox_team.update()
    player_bullet_mgr.update()


def draw():
    global player, background
    clear_canvas()
    background.draw()
    for monster_team in team:
        monster_team.draw()
    for expBox_team in team1:
        expBox_team.draw()

    player_bullet_mgr.draw()
    player.draw()
    update_canvas()
