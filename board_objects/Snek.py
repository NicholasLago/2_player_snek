import pygame


class Snek:

    def __init__(self, colour, location_x, location_y, size):
        self.colour = colour
        self.location_x = location_x
        self.location_y = location_y
        self.direction_x = 0
        self.direction_y = 0
        self.size = size

    def move(self, direction_x, direction_y):
        if direction_x is not 0 or direction_y is not 0:
            self.direction_x = direction_x
            self.direction_y = direction_y

    def draw(self, display):
        self.update()
        pygame.draw.rect(display, self.colour, [self.location_x, self.location_y, self.size, self.size])

    def update(self):
        self.location_x = self.location_x + self.direction_x
        self.location_y = self.location_y + self.direction_y

