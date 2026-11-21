# Example file showing a circle moving on screen
import pygame
from src.player import Player

### setup routine
# init components
# draw field

print("\n***** INITIALIZATION *****\n")
# pygame setup
try:
    pygame.init()
except Exception as e:
    print(f"Error: {e}")

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
delta_time = 0


player1_pos = pygame.Vector2(screen.get_width() / 4, screen.get_height() / 4 * 3)
player2_pos = pygame.Vector2(screen.get_width() / 4 * 3, screen.get_height() / 4 * 3)

net_top = pygame.Vector2(screen.get_width() / 2, (3*screen.get_height()) / 4)
net_width = 20
net_bottom = pygame.Vector2(screen.get_width() / 2, screen.get_height())

player1 = Player(
    init_name = "gennaro",
    init_pos = player1_pos,
    init_score = 0,
    init_movement = {
                    'up': pygame.K_w,
                    'down': pygame.K_s,
                    'left': pygame.K_a,
                    'right': pygame.K_d,
                },
    init_color = "red",
)
player2 = Player(
    init_name = "ambrogio",
    init_pos = player2_pos,
    init_score = 0,
    init_movement = {
                    'up': pygame.K_UP,
                    'down': pygame.K_DOWN,
                    'left': pygame.K_LEFT,
                    'right': pygame.K_RIGHT,
                },
    init_color = "blue",
)

pygame.key.set_repeat(50,50)
running = True # activation as last line of setup 

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    #rect(surface, color, rect, width=0, border_radius=0, border_top_left_radius=-1, border_top_right_radius=-1, border_bottom_left_radius=-1, border_bottom_right_radius=-1) -> Rect
    #left, top, width, height
    rect_left = (screen.get_width() - net_width)/ 2
    rect_top = screen.get_height() / 4
    rect_height = screen.get_height()*3/4
    im_a_rect = pygame.Rect((rect_left, rect_top), (net_width, rect_height)) 
    pygame.draw.rect(screen, "white", im_a_rect, width=net_width)
    
    player1.fig_draw(screen)
    player2.fig_draw(screen)
    

    keys = pygame.key.get_pressed()
    player1.move(keys, delta_time)
    player2.move(keys, delta_time)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # delta_time is delta time in seconds since last frame, used for framerate-
    # independent physics.
    delta_time = clock.tick(60) / 1000

pygame.quit()