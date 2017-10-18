import game_framework
import title_state
import random
import numbers

from pico2d import *

name = "TitleState"
image = None

global curIndex
curIndex = -1
global boyIndex
boyIndex = -1

global mouseX, mouseY

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    image = None

    LEFT_RUN, RIGHT_RUN, LEFT_STAND, RIGHT_STAND = 0, 1, 2, 3

    def __init__(self):
       self.x, self.y = random.randint(100, 700), 90
       self.frame = random.randint(0, 7)
       self.dir = 1
       self.state = self.RIGHT_RUN
       self.run_frames = 0
       self.stand_frames = 0
       if Boy.image == None:
           Boy.image = load_image('animation_sheet.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.handle_state[self.state](self)
        #if self.state == self.RIGHT_RUN:
        #    self.frame = (self.frame + 1) % 8
        #    self.x += (self.dir * 5)
        #elif self.state == self.LEFT_RUN:
        #    self.frame = (self.frame + 1) % 8
        #    self.x += (self.dir * 5)

        #if self.x > 800:
        #    self.dir = -1
        #    self.x = 800
        #    self.state = self.LEFT_RUN
        #elif self.x < 0:
        #    self.dir = 1
        #    self.x = 0
        #    self.state = self.RIGHT_RUN

    def draw(self):
        self.image.clip_draw(self.frame * 100, self.state * 100, 100, 100, self.x, self.y)

    def move(self):
        global mouseX, mouseY
        self.x = mouseX
        self.y = mouseY

    def handle_left_run(self):
        self.x -= 5
        self.run_frames += 1
        if self.x < 0:
            self.state = self.RIGHT_RUN
            self.x = 0
        if self.run_frames == 100:
            self.state = self.LEFT_STAND
            self.stand_frames = 0

    def handle_left_stand(self):
        self.stand_frames += 1
        if self.stand_frames == 50:
            self.state = self.LEFT_RUN
            self.run_frames = 0

    def handle_right_run(self):
        self.x += 5
        self.run_frames += 1
        if self.x > 800:
            self.state = self.LEFT_RUN
            self.x = 800
        if self.run_frames == 100:
            self.state = self.RIGHT_STAND
            self.stand_frames = 0

    def handle_right_stand(self):
        self.stand_frames += 1
        if self.stand_frames == 50:
            self.state = self.RIGHT_RUN
            self.run_frames = 0

    handle_state = {
        LEFT_RUN: handle_left_run,
        RIGHT_RUN: handle_right_run,
        LEFT_STAND: handle_left_stand,
        RIGHT_STAND: handle_right_stand
    }



def enter():
    global grass
    create_team()
    #team = [Boy() for i in range(1000)]
    grass = Grass()

def exit():
    global team, grass
    for boy in team:
        del(boy)
    del(grass)



def handle_events():
    events = get_events()
    global mouseX, mouseY
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_SPACE:
                global curIndex
                curIndex = 0
                global boyIndex
                boyIndex = curIndex
            elif event.key == SDLK_DOWN:
                curIndex -= 1
                if curIndex < 0:
                    curIndex = 0
                boyIndex = curIndex
            elif event.key == SDLK_UP:
                curIndex += 1
                if curIndex > 1000:
                    curIndex = 1000
                boyIndex = curIndex
        elif event.type == SDL_MOUSEMOTION:
            mouseX, mouseY = event.x, 600 - event.y

def create_team():
    player_state_tabel = {
        "LEFT_RUN" : Boy.LEFT_RUN,
        "RIGHT_RUN" : Boy.RIGHT_RUN,
        "LEFT_STAND" : Boy.LEFT_STAND,
        "RIGHT_STAND" : Boy.RIGHT_STAND
    }

    team_data_file = open('team_data.txt', 'r')
    team_data = json.load(team_data_file)
    team_data_file.close()

    global team
    team = []

    for name in team_data:
        player = Boy()
        player.name = name
        player.x = team_data[name]['x']
        player.y = team_data[name]['y']
        player.state = player_state_tabel[team_data[name]['StartState']]
        team.append(player)

    return team


def update():
    global team
    for boy in team:
        boy.update()
    delay(0.05)

def draw():
    clear_canvas()
    grass.draw()
    global boyIndex
    if boyIndex > 0:
        team[boyIndex].move()
        boyIndex = -1
    for boy in team:
        boy.draw()
    numbers.draw(curIndex + 1, 740, 540)
    update_canvas()