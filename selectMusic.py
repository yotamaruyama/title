#!/usr/bin/env python
import pygame
from pygame.locals import *
import sys

SCREEN_SIZE = Rect(0, 0, 640, 480)

def main():
    print("Hello World")
    
    pygame.init()
    pygame.display.set_caption("sample")
    screen = pygame.display.set_mode(SCREEN_SIZE.size)
    title_font = pygame.font.Font("data/minamoji04.ttf", 48)
    menu_font = pygame.font.Font("data/minamoji04.ttf", 32)
    credit_font = pygame.font.SysFont(None, 32)

    title = title_font.render(u"わくわくリズム", True, (255, 255, 255))
    start = menu_font.render(u"はじめる", True, (255, 255, 255))
    exit = menu_font.render(u"やめる", True, (255, 255, 255))
    credit = credit_font.render(u"Group Yellow", True, (255, 255, 255))
    screen.fill((0, 0, 0))
    screen.blit(title, ((320 - (title.get_width() / 2)), 100))
    screen.blit(credit, ((320 - (credit.get_width() / 2)), 420))
    screen.blit(start, ((320 - (start.get_width() / 2)), 225))
    screen.blit(exit, ((320 - (exit.get_width() / 2)), 275))

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()   
        
        pygame.display.update()
            


if __name__ == "__main__":
    main()