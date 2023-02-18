#!/usr/bin/env python
import pygame
from pygame.locals import *
import sys
import cursor
import time

class SelectMusic : 

    def __init__(self,screen):
        self.screen = screen
        self.music = ["馬ぴょい","YMCA","粉雪"] 
        """曲名のリスト"""
        self.title_font = pygame.font.Font("data/minamoji04.ttf", 48)
        self.menu_font = pygame.font.Font("data/minamoji04.ttf", 32)
        self.credit_font = pygame.font.SysFont(None, 32)
        self.title = self.title_font.render(u"選曲", True, (255, 255, 255))
        self.music_Choise = [] 
        """曲名をテキスト化する為のリスト"""
        self.number_of_items = self.music.__len__()+1
        """戻るを含めた項目数"""
        self.blank = 50
        """行間を設定"""
        #for i in self.music:
            #self.music_Choise.append(self.menu_font.render(i, True, (255, 255, 255)))

        for j in range(self.music.__len__()):
            self.music_Choise.append(self.menu_font.render(str(j+1)+"."+self.music[j], True, (255, 255, 255)))
            print(str(j+1)+"."+self.music[j])
        #self.start = self.menu_font.render(u"１．馬ぴょい", True, (255, 255, 255))
        self.exit = self.menu_font.render(u"戻る", True, (255, 255, 255))
        self.credit = self.credit_font.render(u"Group Yellow", True, (255, 255, 255))
        
    def gameninit(self) :
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.title, ((320 - (self.title.get_width() / 2)), 100))
        self.screen.blit(self.credit, ((320 - (self.credit.get_width() / 2)), 420))
        for i in range(self.music_Choise.__len__()):
            self.screen.blit(self.music_Choise[i], ((320 - (self.music_Choise[i].get_width() / 2)), 225+self.blank*i))
        #self.screen.blit(self.start, ((320 - (self.start.get_width() / 2)), 225))
        self.screen.blit(self.exit, ((320 - (self.exit.get_width() / 2)), 225+self.blank*self.music_Choise.__len__()))
        self.mycursor = cursor.Cursor(220, 230, (255, 255, 255))
        self.mycursor.draw(self.screen)
        self.select = 0

    def update(self,events):
         for event in events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()   

            if event.type != KEYDOWN:
                continue

            if event.key == K_DOWN:
                self.inputDown()

            if event.key == K_UP:
                self.inputUp()

            
            pygame.display.update()
            self.mycursor.draw(self.screen)
        #self.screen.fill((0, 0, 0))
    def inputUp(self):
        if self.select == 0:
            return
        else:
            self.mycursor.move(self.screen,move_y=-self.blank)
            self.select -= 1

    def inputDown(self):
        
        if self.select == self.number_of_items-1:#カーソルが一番下まで行ったら
            return  
        self.mycursor.move(self.screen,move_y=+self.blank)
        self.select += 1
        

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("sample")
    SCREEN_SIZE = Rect(0, 0, 640, 480)
    screen = pygame.display.set_mode(SCREEN_SIZE.size)        
    mainObj=SelectMusic(screen)
    mainObj.gameninit()
    while True:
        mainObj.update(pygame.event.get())
        pygame.display.update()
        time.sleep(0.001)
        