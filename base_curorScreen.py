#!/usr/bin/env python
import sys

import pygame
from pygame.locals import *

import cursor
from key_parent import key_parent


import abc


class Base_CursorScreen(metaclass=abc.ABCMeta):

    def __init__(self, screen, columNumber):

        self.screen = screen
        self.columNumber = columNumber
        self.title_font = pygame.font.Font("data/minamoji04.ttf", 48)
        self.menu_font = pygame.font.Font("data/minamoji04.ttf", 32)

    def inputUp(self):
        if self.select == 0:
            return
        else:
            self.mycursor.move(self.screen, move_y=-self.blank)
            self.select -= 1

    def inputDown(self):
        if self.select == self.columNumber - 1:  # カーソルが一番下まで行ったら
            return
        self.mycursor.move(self.screen, move_y=+self.blank)
        self.select += 1
