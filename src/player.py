import pygame

PLAYER_SIZE_X = 120
PLAYER_SIZE_Y = 120

PLAYER_SPEED = 300

PLAYER_MAX_POS_X = 600
PLAYER_MIN_POS_X = 0 
PLAYER_MAX_POS_Y = 600
PLAYER_MIN_POS_Y = 0

class Player:
    name, pos, score, color = None, None, None, None
    count = 0
    id = 0
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
        # self.name = init_name
        Player.count += 1
        self.id = Player.count
        self.name = f"Player {self.id}"
        self.pos = init_pos
        self.score = init_score
        self.movement = init_movement
        self.color = init_color
        self.player_fig = pygame.image.load("p.png")
        self.player_fig = pygame.transform.smoothscale(self.player_fig, (PLAYER_SIZE_X, PLAYER_SIZE_Y))
        self.rect = self.player_fig.get_rect()
        print(self)

    def __str__(self):
        out = f"name: {self.name}\n"
        out += f"id: {self.id}\n"
        out += f"pos: {self.pos}\n"
        out += f"score: {self.score}\n"
        out += f"color: {self.color}\n"
        out += f"rect: {self.rect}\n"
        return out

    def move(self, keys, delta_time, screen, net):
        # print(f"{self.name}: {self.rect} against net: {net}")
        # up
        if keys[self.movement['up']]:
            self.pos.y -= PLAYER_SPEED * delta_time
            self.pos.y = max(self.pos.y, PLAYER_MIN_POS_Y)

        # down
        if keys[self.movement['down']]:
            self.pos.y += PLAYER_SPEED * delta_time
            self.pos.y = min(self.pos.y, PLAYER_MAX_POS_Y)

        # left
        if keys[self.movement['left']]:
            self.pos.x -= PLAYER_SPEED * delta_time
            if self.id % 2 != 0:
                self.pos.x = max(self.pos.x, 0)
            elif not self.rect.colliderect(net):
                self.pos.x = max(self.pos.x, screen.get_width() / 2)
            # self.pos.x = max(self.pos.x, PLAYER_MAX_POS_X)

        # right
        if keys[self.movement['right']]:
            self.pos.x += PLAYER_SPEED * delta_time
            if self.id % 2 != 0:
                self.pos.x = min(self.pos.x, screen.get_width() / 2 - PLAYER_SIZE_X)
            elif not self.rect.colliderect(net):
                self.pos.x = min(self.pos.x, screen.get_width() - PLAYER_SIZE_X)
            # self.pos.x = min(self.pos.x, PLAYER_MAX_POS_X)
        
        # self.clamp_ip(screen.get_rect())
            
    def draw_player(self, screen):
        screen.blit(self.player_fig, self.pos)
        self.rect = self.player_fig.get_rect()