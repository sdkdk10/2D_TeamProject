from pico2d import *

def collision_distance(src, dest):
    disX = src.posX() - dest.posX()
    disY = src.posY() - dest.posY()
    distance = math.sqrt(disX * disX + disY * disY)
    size = src.getSizeX() + dest.getSizeX()

    if distance < size:
        return True
    return False

