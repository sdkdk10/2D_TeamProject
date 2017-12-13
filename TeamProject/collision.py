from pico2d import *

def collision_distance_A(src, dest):
    disX = src.colX() - dest.colX()
    disY = src.colY() - dest.colY()
    distance = math.sqrt(disX * disX + disY * disY)
    size = src.getTransform().getSizeX() + dest.getTransform().getSizeX()

    size /= 2

    if distance < size:
        dest.setIsDead(True)
        src.setIsDead(True)
        return True
    return False

def collision_distance(srcX, srcY, srcSize, destX, destY, destSize):
    disX = srcX - destX
    disY = srcY - destY
    distance = math.sqrt(disX * disX + disY * disY)
    size = srcSize + destSize

    size /= 2

    if distance < size:
        return True
    return False
