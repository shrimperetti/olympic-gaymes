import pygame

PLAYER_SIZE_X = 120
PLAYER_SIZE_Y = 120

PLAYER_MAX_POS_X = 600
PLAYER_MIN_POS_X = 0 
PLAYER_MAX_POS_Y = 600
PLAYER_MIN_POS_Y = 0

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
        self.player_fig = pygame.image.load("p.png")
        self.player_fig = pygame.transform.smoothscale(self.player_fig, (PLAYER_SIZE_X, PLAYER_SIZE_Y))
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
            self.pos.y = max(self.pos.y, PLAYER_MIN_POS_Y)
        if keys[self.movement['down']]:
            self.pos.y += 300 * delta_time
            self.pos.y = min(self.pos.y, PLAYER_MAX_POS_Y)
        if keys[self.movement['left']]:
            self.pos.x -= 300 * delta_time
            self.pos.x = max(self.pos.x, PLAYER_MIN_POS_X)
        if keys[self.movement['right']]:
            self.pos.x += 300 * delta_time
            self.pos.x = min(self.pos.x, PLAYER_MAX_POS_X)
        
        # self.clamp_ip(screen.get_rect())
            
    def draw_player(self, screen):
        screen.blit(self.player_fig, self.pos)
