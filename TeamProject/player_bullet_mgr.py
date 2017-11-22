import player_bullet
import player

bulletStack = None
global expMonster
expMonster = None
global player

def enter(_monster):
    global monster
    monster = _monster

def add_Monster(_monster):
    global expMonster
    if expMonster == None:
        expMonster = [_monster]
    else:
        expMonster.append(_monster)


def add_bullet(bullet):
    global bulletStack
    global monster
    if bulletStack == None:
        bulletStack = [bullet]
    else:
        #len = len(bulletStack)
        #bulletStack[len] = bullet
        bulletStack.append(bullet)

    bullet.setMonster(monster)

def setPlayer(_player):
    global player
    player = _player

def update():
    global bulletStack
    if bulletStack != None:
        stacklen = len(bulletStack)
        for i in range(stacklen):
            if bulletStack[i].update() == 1:
                #del(bulletStack[i])
                bulletStack.pop(i)
        #iterator = iter(bulletStack)
        #for bullet in iterator:
        #    if bullet.update() == 1:
        #        print("delete()")
        #        del(bullet)




def draw():
    global bulletStack
    if bulletStack != None:
        #stacklen = len(bulletStack)
        #for i in range(stacklen):
        #    bulletStack[i].draw()
        iterator = iter(bulletStack)
        for bullet in iterator:
            #if bullet.getTransform().posX()
            bullet.draw()

def exit():
    global bulletStack
    if bulletStack != None:
        stacklen = len(bulletStack)
        for i in range(stacklen):
            del(bulletStack[i])