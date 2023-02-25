import pygame
from pygame.locals import *

import tools


class Shot(pygame.sprite.Sprite):
    animecycle = 6
    speed = 9

    def __init__(self, pos, direction):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.images = tools.split_image(
            tools.load_image("data", "shot.png"), 4, 1)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.direction = direction
        self.frame = 0

    def update(self):
        if self.direction == 0:
            self.rect.move_ip(-self.speed, 0)
            if self.rect.left <= 0:
                self.kill()
        elif self.direction == 1:
            self.rect.move_ip(self.speed, 0)
            if self.rect.right >= 640 - 32:
                self.kill()
        self.frame += 1
        self.image = self.images[int(self.frame / self.animecycle % 4)]
