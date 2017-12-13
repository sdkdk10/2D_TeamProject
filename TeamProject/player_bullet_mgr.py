import player_bullet
import player

bulletStack = None
global expMonster
expMonster = None
global player

global update_bullet
update_bullet = None

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
        bulletStack.append(bullet)

    bullet.setMonster(monster)

def setPlayer(_player):
    global player
    player = _player

def setExpMonster(_exp):
    global expMonster
    expMonster = _exp

def setMonster(_monster):
    global monster
    monster = _monster

def update():
    global bulletStack
    global update_bullet

    if bulletStack != None:
        update_bullet = [b for b in bulletStack if b.getIsDead() == False]

    if update_bullet != None:
        stacklen = len(update_bullet)
        for i in range(stacklen):
            update_bullet[i].update()



def draw():
    global update_bullet
    if update_bullet != None:
        stacklen = len(update_bullet)
        for i in range(stacklen):
            update_bullet[i].draw()

def exit():
    global bulletStack
    if bulletStack != None:
        for delbullet in bulletStack:
            del(delbullet)