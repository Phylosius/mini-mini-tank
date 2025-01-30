import sys

import pygame

from objects.tank import Tank

sprites_updater = lambda s: s.update()
sprites_drawer = lambda s: s.draw()


class Game:
    def __init__(self, title):
        pygame.init()

        self.title = title
        self.fps = 60
        self.running = True
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.keys = pygame.key.get_pressed()

        self.player_group = pygame.sprite.Group()
        self.bullet_group = pygame.sprite.Group()

    def add_player(self, player):
        self.player_group.add(player)

    def check_bullets_collision_with_players(self):
        for player in self.player_group:
            for bullet in pygame.sprite.spritecollide(player, self.bullet_group, False):
                bullet.hint(player)

    def init(self):
        pygame.display.set_caption(self.title)

    def sprite_group_update(self):
        for player in self.player_group.sprites():
            player.update()
        for bullet in self.bullet_group.sprites():
            bullet.update()

    def draw_surfaces(self):
        for player in self.player_group.sprites():
            player.draw(self.screen)
        for bullet in self.bullet_group.sprites():
            bullet.draw(self.screen)

    def update(self):
        self.check_bullets_collision_with_players()
        self.sprite_group_update()

    def run(self):
        self.init()

        while self.running:
            self.keys = pygame.key.get_pressed()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()

            self.update()

            self.screen.fill('dark green')
            self.draw_surfaces()

            pygame.display.flip()
            self.clock.tick(self.fps)

