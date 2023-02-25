#!/usr/bin/env python
import sys

import pygame
from pygame.locals import *

import cursor
from key_parent import key_parent


class Playgame(key_parent):

    def __init__(self, screen):

        self.screen = screen
        self.title_font = pygame.font.Font("data/minamoji04.ttf", 48)
        self.menu_font = pygame.font.Font("data/minamoji04.ttf", 32)
        self.credit_font = pygame.font.SysFont(None, 32)
        self.title = self.title_font.render(u"わくわくリズム", True, (255, 255, 255))
        self.start = self.menu_font.render(u"はじめる", True, (255, 255, 255))
        self.exit = self.menu_font.render(u"やめる", True, (255, 255, 255))
        self.credit = self.credit_font.render(
            u"Group Yellow", True, (255, 255, 255))

    def gameninit(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(
            self.title, ((320 - (self.title.get_width() / 2)), 100))
        self.screen.blit(
            self.credit, ((320 - (self.credit.get_width() / 2)), 420))
        self.screen.blit(
            self.start, ((320 - (self.start.get_width() / 2)), 225))
        self.screen.blit(self.exit, ((320 - (self.exit.get_width() / 2)), 275))
        self.mycursor = cursor.Cursor(220, 230, (255, 255, 255))
        self.mycursor.draw(self.screen)
        self.select = 0

    def main(self):
        print("Hello World")
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type != KEYDOWN:
                    continue

                if event.key == K_DOWN:
                    self.down_input()
                    self.select = 1 - self.select

                if event.key == K_UP:
                    self.up_input()
                    self.select = 1 - self.select

            pygame.display.update()
            self.mycursor.draw(self.screen)

    def update(self, events):

        pygame.display.update()

    def up_input(self):
        return

    def down_input(self):
        return


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("sample")
    SCREEN_SIZE = Rect(0, 0, 640, 480)
    screen = pygame.display.set_mode(SCREEN_SIZE.size)
    mainObj = Playgame(screen)
    mainObj.gameninit()
    while True:
        mainObj.update(pygame.event.get())
        pygame.display.update()
        pygame.time.delay(20)
