import pygame
from pygame.locals import *
# mathモジュールをインポート
import math

import tools


class Enemy(pygame.sprite.Sprite):
    speed = 5

    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = tools.load_image("data", "haraheris.png", -1)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.angle = 90

    def update(self):
        # 円を描きながら移動する
        self.vx = int(3 * math.cos(math.radians(self.angle)))
        self.vy = int(3 * math.sin(math.radians(self.angle)))
        self.rect.move_ip(self.vx, self.vy)
        self.angle += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)
