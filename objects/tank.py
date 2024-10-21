import sys
import pygame
import math
from objects.entity import Entity


class Tank(Entity, pygame.sprite.Sprite):

    def __init__(self):
        Entity.__init__(self)
        pygame.sprite.Sprite.__init__(self)

        self.x = 50
        self.y = 50
        self.speed = 7
        self.rotation_speed = 2  # Plus petit pour des rotations plus fines
        self.radius = 0

        self.image = pygame.image.load('sprites/tank.png')
        self.image = pygame.transform.scale(self.image, (50, 50))

        self.rect = self.image.get_rect(center=(self.x, self.y))

    def move(self):
        rad_angle = math.radians(self.radius + 90)
        self.x += math.cos(rad_angle) * self.speed
        self.y -= math.sin(rad_angle) * self.speed  # Soustraction car l'axe y est inversé

    def rotate_left(self):
        self.radius += self.rotation_speed
        self.radius %= 360  # Garde l'angle dans les bornes [0, 360]

    def rotate_right(self):
        self.radius -= self.rotation_speed
        self.radius %= 360  # Garde l'angle dans les bornes [0, 360]

    def draw(self, screen):
        rotated_image = pygame.transform.rotozoom(self.image, self.radius, 1)
        screen.blit(rotated_image, rotated_image.get_rect(center=(self.x, self.y)))

    def update(self):
        self.rect.topleft = (self.x, self.y)
