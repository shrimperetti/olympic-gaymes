import pygame

PLAYER_SIZE_X = 40
PLAYER_SIZE_Y = 40

class Player:
    name, pos, score, color = None, None, None, None
    movement = {
        'up': None,
        'down': None,
        'left': None,
        'right': None,
    }

    def __init__(self,
                init_name="mario",
                init_pos=pygame.Vector2(0, 0),
                init_score=0,
                init_movement = {
                    'up': pygame.K_UP,
                    'down': pygame.K_DOWN,
                    'left': pygame.K_LEFT,
                    'right': pygame.K_RIGHT,
                },
                init_color="red"):
        self.name = init_name
        self.pos = init_pos
        self.score = init_score
        self.movement = init_movement
        self.color = init_color
        print(self)

    def __str__(self):
        out = f"name: {self.name}\n"
        out += f"pos: {self.pos}\n"
        out += f"score: {self.score}\n"
        out += f"color: {self.color}\n"
        return out

    def move(self, keys, delta_time):
        if keys[self.movement['up']]:
            self.pos.y -= 300 * delta_time
        if keys[self.movement['down']]:
            self.pos.y += 300 * delta_time
        if keys[self.movement['left']]:
            self.pos.x -= 300 * delta_time
        if keys[self.movement['right']]:
            self.pos.x += 300 * delta_time
            
    def get_screen_center(screen, offset=0):
        return ((screen.get_width() / 2) + offset, (screen.get_height() / 2) + offset)
    
    def fig_draw(self, screen):
        pygame.draw.circle(screen, self.color, self.pos, PLAYER_SIZE_X)