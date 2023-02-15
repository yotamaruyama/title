import pygame
from pygame.locals import *
import os
import cv2

def load_image(dir, filename, colorkey=None):
    file = os.path.join(dir, filename)
    image = pygame.surfarray.make_surface(cv2.imread(file))
    #image = pygame.image.load(file)
    image = image.convert()
    if not colorkey == None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image

def split_image(image, n, m):
    image_list = []
    w = image.get_width()
    h = image.get_height()
    w1 = int(w / n)
    h1 = int(h / m)
    for i in range(0, h, h1):
        for j in range(0, w, w1):
            surface = pygame.Surface((w1, h1))
            surface.blit(image, (0, 0), (j, i, w1, h1))
            surface.set_colorkey(surface.get_at((0, 0)), RLEACCEL)
            surface.convert()
            image_list.append(surface)
    return image_list

def play_bgm(file):
    bgm_file = os.path.join("data", file)
    pygame.mixer.music.load(bgm_file)
    pygame.mixer.music.play(-1)

def load_sound(file):
    file = os.path.join("data", file)
    return pygame.mixer.Sound(file)
