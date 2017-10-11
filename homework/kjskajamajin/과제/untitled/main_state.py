from pico2d import *
import title_state
import game_framework
import random
import numbers

class Grass:
    def __init__(self):
        self.image= load_image('grass.png')

    def draw(self):
        self.image.draw(400,30)

class Boy:
    image = None

    LEFT_RUN, RIGHT_RUN, LEFT_STAND, RIGHT_STAND = 0, 1, 2, 3

    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.run_frames = 0
        self.stand_frames = 0
        self.state = self.RIGHT_RUN
        if Boy.image == None:
            Boy.image = load_image('animation_sheet.png')

    def draw(self):
        self.image.clip_draw(self.frame*100, self.state * 100, 100, 100, self.x, self.y)

    def handle_left_run(self):
        self.x -= 5
        self.run_frames += 1
        if self.x < 0:
            self.state = self.RIGHT_RUN
            self.x = 0
        if self.run_frames == 280:
            self.state = self.LEFT_STAND
            self.stand_frames = 0

    def handle_left_stand(self):
        self.stand_frames += 1
        if self.stand_frames == 140:
            self.state = self.LEFT_RUN
            self.run_frames = 0

    def handle_right_run(self):
        self.x += 5
        self.run_frames += 1
        if self.x > 800:
            self.state = self.LEFT_RUN
            self.x = 800
        if self.run_frames == 280:
            self.state = self.RIGHT_STAND
            self.stand_frames = 0

    def handle_right_stand(self):
        self.stand_frames += 1
        if self.stand_frames == 140:
            self.state = self.RIGHT_RUN
            self.run_frames = 0

    handle_state = {
        LEFT_RUN: handle_left_run,
        RIGHT_RUN: handle_right_run,
        LEFT_STAND: handle_left_stand,
        RIGHT_STAND: handle_right_stand
    }

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.handle_state[self.state](self)

    def mouse_update(self):
        self.frame = (self.frame + 1) % 8
        self.x = mouseX
        self.y = mouseY
        self.handle_state[self.state](self)


def enter():
    global boy, grass, team, Tboy, mouseX, mouseY, selectedIndex
    boy = Boy()
    grass = Grass()
    team = [Boy() for i in range(1000)]
    Tboy = 0
    selectedIndex = 0
    mouseX = 0
    mouseY = 0

def exit():
    global boy, grass,selectedIndex, team, Tboy,  mouseX, mouseY
    del(boy)
    del(grass)
    del(team)
    del(Tboy)
    del(mouseX)
    del(mouseY)
    del(selectedIndex)

def handle_events():
    global mouseX
    global mouseY
    global Tboy
    global selectedIndex

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:\
            game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_0:
                Tboy = 0

            elif event.key == SDLK_1:
                Tboy = 1
                selectedIndex = 1
            elif event.key == SDLK_2:
                Tboy = 2
                selectedIndex = 2
            elif event.key == SDLK_3:
                Tboy = 3
                selectedIndex = 3
            elif event.key == SDLK_4:
                Tboy = 4
                selectedIndex = 4

            elif event.key == SDLK_5:
                Tboy = 5
                selectedIndex = 5

            elif event.key == SDLK_6:
                Tboy = 6
                selectedIndex = 6

            elif event.key == SDLK_7:
                Tboy = 7
                selectedIndex = 7

            elif event.key == SDLK_8:
                Tboy = 8
                selectedIndex = 8

            elif event.key == SDLK_9:
                Tboy = 9
                selectedIndex = 9

            elif event.key == SDLK_a:
                Tboy = 10
                selectedIndex = 10

            elif event.key == SDLK_UP:
                Tboy += 1
                selectedIndex += 1

            elif event.key == SDLK_DOWN:
                Tboy -= 1
                selectedIndex -= 1

        elif event.type == SDL_MOUSEMOTION:
            mouseX = event.x
            mouseY = 600 - event.y

def update():
    handle_events()
    if Tboy != None:
        team[Tboy].mouse_update()
    for boy in team:
        boy.update()



def draw():
    clear_canvas()
    grass.draw()
    if Tboy != None:
        team[Tboy].draw()
    for boy in team:
        boy.draw()

    numbers.draw(selectedIndex + 1, 740, 540)

    update_canvas()
