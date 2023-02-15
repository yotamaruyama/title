import pygame
from pygame.locals import *

class Cursor():
    MOVE_RANGE = 15
    speed = 1

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.left = self.x
        self.right = self.x + self.MOVE_RANGE

    def update(self):
        self.x += self.speed
        if self.x < self.left or self.x > self.right:
            self.speed = -self.speed

    def draw(self, screen):
        pygame.draw.polygon(screen, self.color, ([self.x, self.y], [self.x, self.y + 20], [self.x + 20, self.y + 10]))
