#!/usr/bin/env python
import pygame
from pygame.locals import *
import sys
import cursor

class SelectMusic : 

    def __init__(self,screen):
        self.screen = screen

    def update(self,events):
         for event in events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()   

            if event.type != KEYDOWN:
                continue

            if event.key == K_DOWN:
                self.inputDown()
                self.select = 1 - self.select

            if event.key == K_UP:
                self.inputUp()
                self.select = 1 - self.select

            
            pygame.display.update()
            self.mycursor.draw(self.screen)
        #self.screen.fill((0, 0, 0))