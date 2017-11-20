import player_bullet

bulletStack = None

def enter(_monster):
    global monster
    monster = _monster

def add_bullet(bullet):
    global bulletStack
    global monster
    if bulletStack == None:
        bulletStack = [bullet]
    else:
        bulletStack.append(bullet)

    bullet.setMonster(monster)

def update():
    global bulletStack
    if bulletStack != None:
        stacklen = len(bulletStack)
        for i in range(stacklen):
            bulletStack[i].update()

def draw():
    global bulletStack
    if bulletStack != None:
        stacklen = len(bulletStack)
        for i in range(stacklen):
            bulletStack[i].draw()

def exit():
    global bulletStack
    if bulletStack != None:
        stacklen = len(bulletStack)
        for i in range(stacklen):
            del(bulletStack[i])