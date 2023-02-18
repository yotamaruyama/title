#!/usr/bin/env python
import pygame
from pygame.locals import *
import sys
import cursor
from Start import Title
from SelectMusic import SelectMusic

class GameMain:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("sample")
        SCREEN_SIZE = Rect(0, 0, 640, 480)
        self.screen = pygame.display.set_mode(SCREEN_SIZE.size)        
        self.titleScreen = Title(self.screen)
        self.selectMusicScreen = SelectMusic(self.screen)
        self.mode = "Title"
    
    def update(self):
        
        events = pygame.event.get()
        for event in events :
               if event.type == QUIT:
                   pygame.quit()
                   sys.exit()   

               if event.type != KEYDOWN:
                   continue

               if event.key == K_a:
                   self.mode = "SelectMusic"


           
        if self.mode == "Title":
            self.titleScreen.update(events)
            
        elif self.mode == "SelectMusic":
            self.selectMusicScreen.update(events)


   #     elif self.mode == "SelectMusic":
    def main(self):
        self.titleScreen.init()
        while True:
            self.update()
           
            pygame.display.update()
        
if __name__ == "__main__":
    
    mainObj=GameMain()
    mainObj.main()