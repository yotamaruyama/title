import pygame
from pygame.locals import *

class HealthBar():
    def __init__(self, x, y, width, max):
        self.x = x
        self.y = y
        self.width = width
        self.max = max # 最大HP
        self.hp = max # HP
        self.mark = int((self.width - 4) / self.max) # HPバーの1目盛り

        self.font = pygame.font.SysFont(None, 28)
        self.label = self.font.render("HP", True, (255, 255, 255))
        self.frame = Rect(self.x + 2 + self.label.get_width(), self.y, self.width, self.label.get_height())
        self.bar = Rect(self.x + 4 + self.label.get_width(), self.y + 2, self.width - 4, self.label.get_height() - 4)
        self.value = Rect(self.x + 4 + self.label.get_width(), self.y + 2, self.width - 4, self.label.get_height() - 4)

        # effect_barを追加
        self.effect_bar = Rect(self.x + 4 + self.label.get_width(), self.y + 2, self.width - 4, self.label.get_height() - 4)
        self.effect_color = (0, 255, 255)

    def update(self):
        if self.hp >= self.max:
            self.hp = self.max
            
        if self.effect_bar.width > self.mark * self.hp:
            self.value.width = self.mark * self.hp
            if self.effect_bar.width >= self.value.width:
                self.effect_bar.inflate_ip(-1, 0)
        elif self.value.width < self.mark * self.hp:
            self.effect_bar.width = self.mark * self.hp
            self.value.inflate_ip(1, 0)

        # effect_barの色を変える
        if self.effect_bar.width <= self.bar.width / 6:
            self.effect_color = (255, 255, 0)
        elif self.effect_bar.width <= self.bar.width / 2:
            self.effect_color = (255, 255, 0)
        else:
            self.effect_color = (0, 255, 0)

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.frame)
        pygame.draw.rect(screen, (0, 0, 0), self.bar)
        pygame.draw.rect(screen, self.effect_color, self.effect_bar)
        pygame.draw.rect(screen, (0, 0, 255), self.value)
        screen.blit(self.label, (self.x, self.y))
