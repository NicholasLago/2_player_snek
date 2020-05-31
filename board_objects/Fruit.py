import pygame


class Fruit:

    def __init__(self, colour, location_x, location_y, size):
        self.colour = colour
        self.location_x = location_x
        self.location_y = location_y
        self.size = size

    def draw(self, display):
        pygame.draw.rect(display, self.colour, [self.location_x, self.location_y, self.size, self.size])
