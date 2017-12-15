import game_framework
import title_state
import player_bullet_mgr

from player import Player as myPlayer
from background import Background as myBackground
from Monster import Monster as myMonster
from ExpBox import ExpBox as myExpBox
from Boss import Boss as myBoss
from ui_black import UI_Black as myBlack
from ui_font import UI_Font as myFont
from ui_num import UI_Num as myNum
from ui_value import UI_Value as myValue
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
    global boss
    boss = myBoss(background, player)
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

#------------------- UI 관련 --------------------------
    global black_hp_ui
    black_hp_ui = myBlack(600, 80)
    global score_ui
    score_ui = myFont(550, 80, 'Resource/Texture/UI_Font/Score.png')
    global score_num_ui
    score_num_ui = myNum(600, 80, 0.3)
    score_num_ui.setScore(142)
    global hp_ui
    hp_ui = myValue(600, 80, 200, 'Resource/Texture/UI_Bar/Scorebar_Green.png', player, 0.57, 0.8)
    global black_exp_ui
    black_exp_ui = myBlack(600, 50, 1.3, 1.3)
    global exp_ui
    exp_ui = myValue(600, 50, 200, 'Resource/Texture/UI_Bar/Expbar_Yellow.png', player, 1.25, 1)
    player.setExpUI(exp_ui)

def exit():
    global background
    del(background)
    global player
    del(player)
    global Monster
    del(Monster)
    global boss
    del(boss)
    player_bullet_mgr.exit()
    for i in team:
        del(i)
    for i in team1:
        del(i)

    global black_hp_ui, score_ui, score_num_ui, hp_ui, black_exp_ui, exp_ui
    del(black_hp_ui)
    del(score_ui)
    del(score_num_ui)
    del(hp_ui)
    del(black_exp_ui)
    del(exp_ui)

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
    global Exp_update, Mon_update, Boss_update
    Exp_update = [e for e in team1 if e.getIsDead() == False]
    Mon_update = [m for m in team if m.getIsDead() == False]
    player_bullet_mgr.setExpMonster(Exp_update)
    player_bullet_mgr.setMonster(Mon_update)
    boss.update()
    player.update()
    background.update()
    for monster_team in Mon_update:
        monster_team.update()
    for exp_team in Exp_update:
        exp_team.update()
    player_bullet_mgr.update()

def draw():
    global player, background
    global Exp_update, Mon_update
    global black_hp_ui, score_ui, score_num_ui, hp_ui, black_exp_ui
    clear_canvas()
    background.draw()
    player_bullet_mgr.draw()
    for monster_team in Mon_update:
        if monster_team.isInWindow() == True:
            monster_team.draw()
    for expBox_team in Exp_update:
        if expBox_team.isInWindow() == True:
            expBox_team.draw()
    boss.draw()
    player.draw()

    #--------UI 그리기----------
    # HP UI
   #black_hp_ui.draw()
   #hp_ui.draw()
   #score_ui.draw()
   #score_num_ui.draw()

    # EXP UI
    black_exp_ui.draw()
    exp_ui.draw()

    update_canvas()
