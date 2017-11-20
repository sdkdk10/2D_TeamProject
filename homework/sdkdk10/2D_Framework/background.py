import json
from pico2d import *

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