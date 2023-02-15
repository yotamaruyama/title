import pygame
from pygame.locals import *
import sys

import cursor

class Title():
    def __init__(self):
        self.frame = 0
        self.select = 0
        self.title_font = pygame.font.Font("data/minamoji04.ttf", 48)
        self.menu_font = pygame.font.Font("data/minamoji04.ttf", 32)
        self.credit_font = pygame.font.SysFont(None, 32)

        self.title = self.title_font.render(u"わくわくリズム", True, (255, 255, 255))
        self.start = self.menu_font.render(u"はじめる", True, (255, 255, 255))
        self.exit = self.menu_font.render(u"やめる", True, (255, 255, 255))
        self.credit = self.credit_font.render(u"Group Yellow", True, (255, 255, 255))

        self.cursor = cursor.Cursor(220, 230, (255, 255, 255))

    def update(self):
        self.frame += 1
        if self.select == 0:
            self.cursor.y = 230
        elif self.select == 1:
            self.cursor.y = 280

    def draw(self, screen):
        screen.fill((0, 0, 0))
        screen.blit(self.title, ((320 - (self.title.get_width() / 2)), 100))
        screen.blit(self.credit, ((320 - (self.credit.get_width() / 2)), 420))
        screen.blit(self.start, ((320 - (self.start.get_width() / 2)), 225))
        screen.blit(self.exit, ((320 - (self.exit.get_width() / 2)), 275))
        self.cursor.draw(screen)
