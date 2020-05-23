import pygame

from board_objects.Snek import Snek
from board_objects.Fruit import Fruit

TILE_SIZE = 10
TILE = [TILE_SIZE, TILE_SIZE, TILE_SIZE, TILE_SIZE]


def start():
    pygame.init()
    display = create_window(1)
    clock = pygame.time.Clock()
    running = True
    snek_1 = Snek(get_colour("blue"), 0, 0, TILE_SIZE)
    snek_2 = Snek(get_colour("red"), TILE_SIZE*2, TILE_SIZE*2, TILE_SIZE)
    fruit_1 = Fruit(get_colour("pink"), TILE_SIZE*4, TILE_SIZE*6, TILE_SIZE*2)
    game_objects = [fruit_1, snek_1, snek_2]
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                direction = move_1(event.key)
                snek_1.move(direction[0], direction[1])
                direction = move_2(event.key)
                snek_2.move(direction[0], direction[1])

        # Update visuals
        display.fill(get_colour("white"))
        for game_object in game_objects:
            game_object.draw(display)
        pygame.display.update()
        clock.tick(30)

    pygame.quit()
    quit()


def create_window(scale):
    size = 500
    return pygame.display.set_mode((size * scale, size * scale))


def get_colour(colour):
    if colour == "blue":
        return 0, 0, 225
    elif colour == "red":
        return 225, 0, 0
    elif colour == "white":
        return 225, 225, 225
    elif colour == "pink":
        return 255, 192, 203


def move_1(key):
    if key == pygame.K_UP:
        return [0, -TILE_SIZE]
    elif key == pygame.K_DOWN:
        return [0, TILE_SIZE]
    elif key == pygame.K_RIGHT:
        return [TILE_SIZE, 0]
    elif key == pygame.K_LEFT:
        return [-TILE_SIZE, 0]
    return [0, 0]

def move_2(key):
    if key == pygame.K_e:
        return [0, -TILE_SIZE]
    if key == pygame.K_d:
        return [0, TILE_SIZE]
    if key == pygame.K_f:
        return [TILE_SIZE, 0]
    if key == pygame.K_s:
        return [-TILE_SIZE, 0]
    return [0, 0]



start()