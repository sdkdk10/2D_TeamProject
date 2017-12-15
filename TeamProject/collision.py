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

def boundingbox(self):
    return self.scrollX - 10, self.scrollY - 10, self.scrollX + 10, self.scrollY + 10

def collision(a,b):
    left_a, bottom_a, right_a, top_a = a.boundingbox()
    left_b, bottom_b, right_b, top_b = b.boundingbox()
    if left_a > right_b:
        return False
    elif right_a < left_b:
        return False
    elif top_a < bottom_b:
        return False
    elif bottom_a < top_b:
        return False
    return True