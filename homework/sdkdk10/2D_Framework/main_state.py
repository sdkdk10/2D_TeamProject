import game_framework
import title_state
import random
import json
import cProfile
#from background import Background

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

class Background:
    def draw(self):
        x = int(self.left)
        w = min(self.image.w - x, self.screen_width)
        self.image.clip_draw_to_origin(x, 0, w, self.screen_height, 0, 0)
        self.image.clip_draw_to_origin(0,0, self.screen_width, self.screen_height, w,0)

    def update(self, frame_time):
        self.left= (self.left + frame_time * self.speed) % self.image.w


class TileBackground:
    SCROLL_SPEED_PPS = 10

    def __init__(self, filename, width, height):
        f = open(filename)
        self.map = json.load(f)
        self.x = 0
        self.y = 0
        self.canvasWidth = width
        self.canvasHeight = height
        image_filename = self.map['tilesets'][0]['image']
        self.image = load_image(image_filename)
        self.speedX = 0
        self.speedY = 0
        self.dirX = 0
        self.dirY = 0
        self.bgm = load_music('football.mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()
        self.pickSound = load_wav('pickup.wav')
        self.pickSound.set_volume(32)

    def draw(self):
        tile_per_line = self.map['width']
        map_height = self.map['height']
        map_width = self.map['width']
        data = self.map['layers'][0]['data']
        tileset = self.map['tilesets'][0]
        tile_width = tileset['tilewidth']
        tile_height = tileset['tileheight']
        margin = tileset['margin']
        spacing = tileset['spacing']
        columns = tileset['columns']

        self.speedX += TileBackground.SCROLL_SPEED_PPS * self.dirX
        self.speedY += TileBackground.SCROLL_SPEED_PPS * self.dirY
        #------------------------------------------------------
        rows = -(-tileset['tilecount'] // columns) # math.ceil()

        startx = tile_width // 2 - self.x % tile_width
        starty = tile_height // 2 - self.y % tile_height

        endx = self.canvasWidth + tile_width // 2
        endy = self.canvasHeight + tile_height // 2

        desty = starty
        my = int(self.y // tile_height)
        while(desty < endy):
            destx = startx
            mx = int(self.x // tile_width)
            while(destx < endx):
                index = (map_height - my - 1) * map_width - mx
                tile = data[index]
                tx = (tile - 1) % columns
                ty = rows - (tile - 1) // columns - 1
                srcx = margin + tx * (tile_width + spacing)
                srcy = margin + ty * (tile_height + spacing)
                self.image.clip_draw(srcx, srcy, tile_width, tile_height, destx + self.speedX, desty + self.speedY)
                destx += tile_width
                mx += 1
            desty += tile_height
            my += 1

        #------------------------------------------------------

        #dx, dy = 0 + tile_width / 2, 0 + tile_height / 2
        #desty = dy
        #print("========================")
        #y = 0
        #while(desty < self.canvasHeight):
        #    destx = dx
        #    x = 0
        #    while(destx < self.canvasWidth):
        #        index = (map_height - y - 1) * tile_per_line + x
        #        tile = data[index]
        #        tx = (tile - 1) % columns
        #        ty = (tile - 1) // columns
        #        srcx = margin + tx * (tile_width + spacing)
        #        srcy = self.image.h - (margin + ty * (tile_height + spacing))
        #        #(srcx, srcy, tile_width, tile_height)
        #        #(destx, desty)
        #        self.image.clip_draw(srcx, srcy, tile_width, tile_height, destx, desty)
        #        destx += tile_width
        #        print(x, y, index, tile, srcx, srcy, destx, desty)
        #        x + 1
        #    desty += tile_height
        #    y + 1

    def handle_event(self, event):
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_LEFT:
                self.dirX = 1
                self.pickSound.play()
            if event.key == SDLK_RIGHT:
                self.dirX = -1
            if event.key == SDLK_UP:
                self.dirY = -1
            if event.key == SDLK_DOWN:
                self.dirY = 1

        if event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT or event.key == SDLK_RIGHT:
                self.dirX = 0
            if event.key == SDLK_UP or event.key == SDLK_DOWN:
                self.dirY = 0
#
class Boy:
    PIXEL_PER_METER = (10.0 / 0.3)          #10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0                   # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8
    image = None

    LEFT_RUN, RIGHT_RUN, LEFT_STAND, RIGHT_STAND = 0, 1, 2, 3

    def __init__(self):
       self.x, self.y = 400, 90
       self.frame = random.randint(0, 7)
       self.dir = 1
       self.state = self.RIGHT_RUN
       self.run_frames = 0
       self.stand_frames = 0
       self.total_frames = 0
       if Boy.image == None:
           Boy.image = load_image('animation_sheet.png')

    def update(self, frame_time):
        distance = Boy.RUN_SPEED_PPS * frame_time
        self.total_frames += Boy.FRAMES_PER_ACTION * Boy.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 8

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

    def handle_event(self, event):
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_LEFT:
                self.state = self.LEFT_RUN
            elif event.key == SDLK_RIGHT:
                self.state = self.RIGHT_RUN
        if event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT:
                self.state = self.LEFT_STAND
            elif event.key == SDLK_RIGHT:
                self.state = self.RIGHT_STAND

class Button:
    def __init__(self, imageFilename, x = 0, y = 0):
        self.image = load_image(imageFilename)
        self.x, self.y = x, y

    def draw(self):
        self.image.draw(self.x, self.y)

    def handle_event(self, event):
        if event.type == SDL_MOUSEMOTION:
            if(self.ptInRect(mouse.x, mouse.y)):
                self.onOver()

    def onOver(self):
        print("on Over")

    def ptInRect(self, x, y):
        if(x < self.x - self.image.w / 2):
            return False
        if(x > self.x + self.image.w / 2):
            return False
        if(y < self.y - self.image.h / 2):
            return False
        if(y > self.y + self.image.h / 2):
            return False
        return True

def enter():
    global grass, boy
    grass = TileBackground('map.json', 800, 600)
    boy = Boy()
    global button, button2
    button = uif.Button('insta.png', 400, 300)
    button.onOver = onBtnInsta
    button2 = uif.Button('twit.png', 600, 300)
    button2.onOver = onBtnTwit

def onBtnInsta():
    print("On Insta")

def onBtnTwit():
    print("On Twit")

def exit():
    global team, grass, boy
    del(grass)
    del(boy)



def handle_events():
    events = get_events()
    global mouseX, mouseY
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type == SDL_MOUSEMOTION:
            mouseX, mouseY = event.x, 600 - event.y
        else:
            global boy
            global grass
            #boy.handle_event(event)
            grass.handle_event(event)

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

global current_time
current_time = get_time()



def update():
    #global team
    #global current_time
#
    #frame_time = get_time() - current_time
    #frame_rate = 1.0 / frame_time
    #print("Frame Rate : %f fps, Frame Time : %f sec, " %(frame_rate, frame_time))
#
    #current_time += frame_time
#
    #grass.update(frame_time)
#
    #boy.update(frame_time)

    delay(0.3)

def draw():
    clear_canvas()
    grass.draw()
    #global boyIndex
    #if boyIndex > 0:
    #    team[boyIndex].move()
    #    boyIndex = -1
    ##boy.draw()
    update_canvas()