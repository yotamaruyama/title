#!/usr/bin/env python
import sys

import pygame
from pygame.locals import *
from playgame import Playgame

from selectMusic import SelectMusic
from Start import Title


class GameMain:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("sample")
        SCREEN_SIZE = Rect(0, 0, 640, 480)
        self.screen = pygame.display.set_mode(SCREEN_SIZE.size)
        self.titleScreen = Title(self.screen, self)
        self.selectMusicScreen = SelectMusic(self.screen, self)
        self.playgame = Playgame(self.screen,self)
        self.mode = "Title"
        self.musicnumber = -1


    def update(self):

        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type != KEYDOWN:
                continue

        if self.mode == "Title":
            self.titleScreen.update(events)

        elif self.mode == "SelectMusic":
            self.selectMusicScreen.update(events)

        elif self.mode == "playgame":
            self.playgame.update(events)

   #     elif self.mode == "SelectMusic":

    def main(self):
        self.titleScreen.gameninit()
        while True:
            self.update()
            pygame.time.delay(20)
            pygame.display.update()

    def gamenseni(self, mode):
        self.mode = mode
        if mode == "Title":
            self.titleScreen.gameninit()

        elif mode == "SelectMusic":
            self.selectMusicScreen.gameninit()

        elif mode == "playgame":
            self.playgame.gameninit()


if __name__ == "__main__":

    mainObj = GameMain()
    mainObj.main()
    print(mainObj.mode)
