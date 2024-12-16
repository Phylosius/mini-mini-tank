import sys

import pygame

from objects.tank import Tank


class Game:
    def __init__(self, title):
        pygame.init()

        self.title = title
        self.fps = 60
        self.running = True
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.keys = pygame.key.get_pressed()

        self.player = Tank(self)
        self.player_group = pygame.sprite.Group()
        self.bullet_group = pygame.sprite.Group()

    def check_keywords(self):

        if self.keys[pygame.K_UP]:
            self.player.move()

        if self.keys[pygame.K_LEFT]:
            self.player.rotate_left()
        elif self.keys[pygame.K_RIGHT]:
            self.player.rotate_right()

    def init(self):
        pygame.display.set_caption(self.title)
        self.player_group.add(self.player)

    def draw_surfaces(self):
        for player in self.player_group.sprites():
            player.draw(self.screen)
        for bullet in self.bullet_group.sprites():
            bullet.draw(self.screen)

    def update(self):
        self.check_keywords()
        self.player_group.update()
        for bullet in self.bullet_group.sprites():
            bullet.update()

    def run(self):
        self.init()

        while self.running:
            self.keys = pygame.key.get_pressed()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.player.shoot()

            self.update()

            self.screen.fill('dark green')
            self.draw_surfaces()

            pygame.display.flip()
            self.clock.tick(self.fps)

