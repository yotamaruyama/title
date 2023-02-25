#!/usr/bin/env python
import pygame
from pygame.locals import *
import sys

import cursor
import tools
import player
import enemy
import bar
import shot
import title

SCR_RECT = Rect(0, 0, 640, 480)
TITLE, STAGE = range(2)


class Main():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("sample")
        screen = pygame.display.set_mode(SCR_RECT.size)

        self.all = pygame.sprite.RenderUpdates()
        self.enemies = pygame.sprite.Group()
        self.shots = pygame.sprite.Group()
        player.Player.containers = self.all
        enemy.Enemy.containers = self.all, self.enemies
        shot.Shot.containers = self.all, self.shots

        self.enemy_1 = enemy.Enemy((150, 80))
        self.enemy_2 = enemy.Enemy((330, 400))
        self.player = player.Player((288, 200))

        self.bg = tools.load_image("data", "bg.png")
        self.bgx = 0
        self.scroll_speed = 3

        self.hp = bar.HealthBar(32, 32, 100, 12)

        self.load_sounds()
        tools.play_bgm("bgm.ogg")

        # タイトル画面をインスタンス化
        self.title = title.Title()

        clock = pygame.time.Clock()
        global game_state
        game_state = TITLE
        while True:
            clock.tick(30)
            self.update()
            self.draw(screen)
            pygame.display.update()
            self.key_handler()

    def update(self):
        global game_state
        if game_state == TITLE:
            self.title.update()
        elif game_state == STAGE:
            self.bgx = (self.bgx - self.scroll_speed) % SCR_RECT.width
            self.all.update()
            self.collision_detection()
            self.hp.update()

    def draw(self, screen):
        global game_state
        if game_state == TITLE:
            self.title.draw(screen)
        elif game_state == STAGE:
            screen.blit(self.bg, (self.bgx, 0))
            screen.blit(self.bg, (self.bgx - SCR_RECT.width, 0))
            self.all.draw(screen)
            self.hp.draw(screen)

    def key_handler(self):
        global game_state
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and event.key == K_SPACE:
                self.hp.hp += 1

            if game_state == TITLE:
                if event.type == KEYUP and event.key == K_SPACE:
                    if self.title.select == 0:
                        game_state = STAGE
                    elif self.title.select == 1:
                        pygame.quit()
                        sys.exit()
                elif event.type == KEYDOWN and event.key == K_UP:
                    if self.title.select > 0:
                        self.title.select -= 1
                elif event.type == KEYDOWN and event.key == K_DOWN:
                    if self.title.select < 1:
                        self.title.select += 1

    def collision_detection(self):
        enemy_collided = pygame.sprite.spritecollide(
            self.player, self.enemies, False)
        if enemy_collided:
            if self.player.invincible == False:
                # SEを再生する
                self.damage_sound.play()
                self.hp.hp -= 1
                self.player.invincible = True
        # 弾と敵との当たり判定
        shot_collided = pygame.sprite.groupcollide(
            self.enemies, self.shots, True, True)

    def load_sounds(self):
        self.damage_sound = tools.load_sound("damage.wav")


if __name__ == "__main__":
    Main()
