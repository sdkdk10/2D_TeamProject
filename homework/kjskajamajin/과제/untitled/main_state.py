from pico2d import *
import game_framework
import title_state
import random

name = "TitleState"
#image = None

class Num:
    def __init__(self):
        self.image = load_image('0.png')

    def draw(self):
        self.image.draw(40, 550)

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    image = None
    LEFT_RUN, RIGHT_RUN, LEFT_STAND , RIGHT_STAND = 0 , 1,2,3


    def __init__(self):
       self.x, self.y = random.randint(100, 700), 90
       self.frame = random.randint(0, 7)
       self.run_frames = 0
       self.stand_frames = 0
       self.state = self.RIGHT_RUN
       if Boy.image == None:
            Boy.image = load_image('animation_sheet.png')

    def handle_left_run(self):
        self.x -= 5
        self.run_frames += 1
        if self.x < 0:
            self.state = self.RIGHT_RUN
            self.x = 0
        if self.run_frames == 480:
            self.state = self.LEFT_STAND
            self.stand_frames = 0

    def handle_left_stand(self):
        self.stand_frames += 1
        if self.stand_frames == 240:
            self.state = self.LEFT_RUN
            self.run_frames = 0

    def handle_right_run(self):
        self.x += 5
        self.run_frames += 1
        if self.x > 800:
            self.state = self.LEFT_RUN
            self.x = 800
        if self.run_frames == 480:
            self.state = self.RIGHT_STAND
            self.stand_frames = 0

    def handle_right_stand(self):
        self.stand_frames += 1
        if self.stand_frames == 240:
            self.state = self.RIGHT_RUN
            self.run_frames = 0

    handle_state = {
            LEFT_RUN: handle_left_run,
            RIGHT_RUN: handle_right_run,
            LEFT_STAND: handle_left_stand,
            RIGHT_STAND: handle_left_stand
        }

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.handle_state[self.state](self)

    def draw(self):
        self.image.clip_draw(self.frame *100, self.state * 100, 100, 100, self.x, self.y)

def enter():
    global boy, grass, team, Tboy, Num, TNum
    boy = Boy()
    grass = Grass()
    team = [Boy() for i in range(1000)]
    Tboy = 0
    Num = Num()
    TNum = 0

def exit():
    global boy, grass, team, Tboy, Num,TNum
    del(boy)
    del(grass)
    del(team)
    del(Tboy)
    del(Num)
    del(TNum)

def handle_events():
    global mouseX
    global mouseY
    global boyNum

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:\
            game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_0:
                Tboy = 0
                TNum = 0
                if TNum == 0:
                    Num.image = load_image('0.png')
            elif event.key == SDLK_1:
                Tboy = 1
                TNum = 1
                if TNum == 1:
                    Num.image = load_image('1.png')
            elif event.key == SDLK_2:
                Tboy = 2
                TNum = 2
                if TNum == 2:
                    Num.image = load_image('2.png')
            elif event.key == SDLK_3:
                Tboy = 3
                TNum = 3
                if TNum == 3:
                    Num.image = load_image('3.png')
            elif event.key == SDLK_4:
                Tboy = 4
                TNum = 4
                if TNum == 4:
                    Num.image = load_image('4.png')
            elif event.key == SDLK_5:
                Tboy = 5
                TNum = 5
                if TNum == 5:
                    Num.image = load_image('5.png')
            elif event.key == SDLK_6:
                Tboy = 6
                TNum = 6
                if TNum == 6:
                    Num.image = load_image('6.png')
            elif event.key == SDLK_7:
                Tboy = 7
                TNum = 7
                if TNum == 7:
                    Num.image = load_image('7.png')
            elif event.key == SDLK_8:
                Tboy = 8
                TNum = 8
                if TNum == 8:
                    Num.image = load_image('8.png')
            elif event.key == SDLK_9:
                Tboy = 9
                TNum = 9
                if TNum == 9:
                    Num.image = load_image('9.png')
            elif event.key == SDLK_F1:
                Tboy = 10
                TNum = 10
                if TNum == 10:
                    Num.image = load_image('10.png')
            elif event.key == SDLK_UP:
                Tboy

            elif event.key == SDLK_DOWN:
                Tboy

        elif event.type == SDL_MOUSEMOTION:
            mouseX = event.x
            mouseY = 600 - event.y

def update():
        handle_events()

        if Tboy != None:
            team[Tboy].update()

def main():

    open_canvas()
    boy = Boy()
    grass = Grass()

    global running
    running = True
    while running:
        handle_events()

        clear_canvas()
        grass.draw()
        boy.draw()
        update_canvas()

        delay(0.05)

    close_canvas()

if __name__ == '__main__':
    main()

def draw():
    clear_canvas()
    grass.draw()
    Num.draw()
    for i in team:
        if Tboy != None:
            team[Tboy].draw()
    update_canvas()
