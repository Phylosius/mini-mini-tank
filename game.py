import sys

import pygame


class DisplayedGame:
    def __init__(self, title):
        pygame.init()

        self.title = title
        self.fps = 60
        self.running = True
        self.screen = None
        self.clock = pygame.time.Clock()
        self.keys = pygame.key.get_pressed()

        self.player_group = pygame.sprite.Group()
        self.bullet_group = pygame.sprite.Group()
        self.display = True

    def init(self):
        pass

    def handle_pygame_event(self, event):
        pass

    def add_player(self, player):
        self.player_group.add(player)

    def init_display(self):
        self.screen = pygame.display.set_mode((800, 600))
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
        self.sprite_group_update()

    def run(self):
        if self.display:
            self.init_display()

        self.init()

        while self.running:
            self.keys = pygame.key.get_pressed()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()

                self.handle_pygame_event(event)

            self.update()

            if self.display:
                self.screen.fill('dark green')
                self.draw_surfaces()

                pygame.display.flip()

            self.clock.tick(self.fps)

