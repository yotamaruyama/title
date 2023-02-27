import pygame
from pygame.locals import *

import tools
import shot


class Player(pygame.sprite.Sprite):
    speed = 5
    frame = 0
    animecycle = 24
    invincible_time = 64
    # リロード時間
    reload_time = 15

    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.images = tools.split_image(
            tools.load_image("data", "rabipple.png"), 2, 2)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.direction = 0
        self.invincible = False
        # リロード時間
        self.reload_timer = 0

    def update(self):
        self.frame += 1
        self.image = self.images[(self.direction * 2) +
                                 int(self.frame / self.animecycle % 2)]
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LEFT]:
            self.frame += 1
            self.direction = 0
            self.rect.move_ip(-self.speed, 0)
        if pressed_keys[K_RIGHT]:
            self.frame += 1
            self.direction = 1
            self.rect.move_ip(self.speed, 0)
        if pressed_keys[K_UP]:
            self.frame += 1
            self.rect.move_ip(0, -self.speed)
        if pressed_keys[K_DOWN]:
            self.frame += 1
            self.rect.move_ip(0, self.speed)
        self.rect.clamp_ip(Rect(0, 0, 640, 480))

        # リロード時間を減らす
        if self.reload_timer > 0:
            self.reload_timer -= 1
        # リロード時間が0なら発射
        if pressed_keys[K_SPACE]:
            if self.reload_timer == 0:
                shot.Shot(self.rect.center, self.direction)
                self.reload_timer = self.reload_time

        if self.invincible == True:
            if self.invincible_time == 0:
                self.invincible = False
                self.invincible_time = Player.invincible_time
            else:
                self.invincible_time -= 1

    def draw(self, screen):
        if self.invincible == False:
            screen.blit(self.image, self.rect)
