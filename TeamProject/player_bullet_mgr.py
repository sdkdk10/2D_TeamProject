import player_bullet

class Player_Bullet_Mgr:
    def __init__(self):
        self.stack = None

    def add_bullet(self, bullet):
        self.stack.append(bullet)

    def update(self):
        for i in range(self.stack):
            self.stack[i].update()

    def draw(self):
        for i in range(self.stack):
            self.stack[i].draw()