#!/usr/bin/env python
import pygame
from pygame.locals import *
import sys
import cursor

class SelectMusic : 

    def __init__(self,screen):
        self.screen = screen

    def blackOut(self):
        self.screen.fill((0, 0, 0))