import player_bullet

bulletStack = None

def add_bullet(bullet):
    global bulletStack
    if bulletStack == None:
        bulletStack = [bullet]
    else:
        bulletStack.append(bullet)

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