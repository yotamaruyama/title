import pygame
from pygame.locals import *

class Cursor():
    MOVE_RANGE = 15
    speed = 1

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.left = self.x
        self.right = self.x + self.MOVE_RANGE

    def update(self):
        self.x += self.speed
        if self.x < self.left or self.x > self.right:
            self.speed = -self.speed

    def draw(self, screen):
        pygame.draw.polygon(screen, self.color, ([self.x, self.y], [self.x, self.y + 20], [self.x + 20, self.y + 10]))

    def replace(self,screen,new_x,new_y):
        deleteCursor = Cursor(self.x,self.y,(0,0,0))
        deleteCursor.draw(screen)
        if new_x == None:
            new_x = self.x
        self.x = new_x
        self.y = new_y
        self.draw(screen)

    def delete(self,screen,new_x,new_y):
        self.deleteCursor.draw(screen)
        self.deleteCursor.x = new_x
        self.deleteCursor.y = new_y
    
    def move(self,screen,move_x=0,move_y=0):
        self.replace(screen,self.x + move_x,self.y + move_y)
