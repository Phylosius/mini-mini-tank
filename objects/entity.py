import pygame


class Entity(pygame.sprite.Sprite):
    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        self.max_health = 100
        self.health = self.max_health

        self.x = 50
        self.y = 50

        self.speed = 0

