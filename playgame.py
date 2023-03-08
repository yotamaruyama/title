#!/usr/bin/env python
import sys
sys.path.append('./project_posenet')
from project_posenet.pose_judge import calculate_jointAngles, calculate_leftelbow, pose_check
import tools

import cv2


import pygame
from pygame.locals import *

import cursor
from key_parent import key_parent
from project_posenet.pose_engine import PoseEngine
from PIL import Image
from PIL import ImageDraw
from project_posenet.pose_judge import *

import numpy as np
import os

#矢印速度
notes_speed = 10


class Playgame(key_parent):

    def __init__(self, screen, gameMain):

        self.screen = screen
        self.gameMain = gameMain
        self.title_font = pygame.font.Font("data/minamoji04.ttf", 48)
        self.menu_font = pygame.font.Font("data/minamoji04.ttf", 32)
        self.credit_font = pygame.font.SysFont(None, 32)
        # self.start = self.menu_font.render(u"はじめる", True, (255, 255, 255))
        # self.exit = self.menu_font.render(u"やめる", True, (255, 255, 255))
        self.credit = self.credit_font.render(
            u"Group Yellow", True, (255, 255, 255))
        self.engine = PoseEngine('/home/io-circle/windowapps/title/project_posenet/models/mobilenet/posenet_mobilenet_v1_075_481_641_quant_decoder_edgetpu.tflite')
        self.score = "unko"
        

    def gameninit(self):
        self.image = tools.load_image("data", "yazirusi.png").convert()
        self.cap = cv2.VideoCapture(0)
        self.screen.fill((0, 0, 0))
        self.title = self.title_font.render((str)(self.score), True, (255, 255, 255))
        self.screen.blit(self.title, ((320 - (self.title.get_width() / 2)), 100))
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

                
            pygame.display.update()
            self.mycursor.draw(self.screen)

    def update(self, events):
        #self.screen.fill((0,0,0))
        # 1フレーム毎　読込み
        ret, frame = self.cap.read()
        cv2.imshow("Camera", frame)
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        poses, inference_time = self.engine.DetectPosesInImage(Image.fromarray(frame))
        frame = cv2.rotate(frame,cv2.ROTATE_90_COUNTERCLOCKWISE)
        poseframe = pygame.surfarray.make_surface(frame)
        self.screen.blit(poseframe,(0,0))
        self.screen.blit(self.title, ((320 - (self.title.get_width() / 2)), 100))
        for pose in poses:
            if pose.score < 0.4: continue
            calculate_leftelbow(pose)
            angles = calculate_jointAngles(pose)
            self.score = pose_check(pose,angles)
            self.title = self.title_font.render((str)(self.score), True, (255, 255, 255))

            #print(poses)
        
        
        for event in events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type != KEYDOWN:
                continue

            if event.key == K_DOWN:
                self.down_input()

            if event.key == K_UP:
                self.up_input()

            if event.key == K_RETURN:
                continue

            if event.key == K_ESCAPE:
                self.kettei()

            pygame.display.update()

    def up_input(self):
        return
    def down_input(self):
        self.score = "timpo"
        self.title = self.title_font.render((str)(self.score), True, (255, 255, 255))

    def aruduino_btn(self):
        return

    def kettei(self):
        self.gameMain.gamenseni("SelectMusic")


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
