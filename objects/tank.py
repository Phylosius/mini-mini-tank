import sys
import pygame
import math

import game
from objects.bullet import Bullet
from objects.entity import Entity


class Tank(Entity):

    def __init__(self, _game):
        Entity.__init__(self)

        self.x = 50
        self.y = 50
        self.speed = 7
        self.rotation_speed = 5  # Plus petit pour des rotations plus fines
        self.radius = -67

        self.game = _game

        self.image_path = 'sprites/tank.png'
        self.image_size = (50, 50)
        self.image_radius =  -90
        self.image_scale = 1

        self.image = pygame.image.load(self.image_path)
        self.image = pygame.transform.scale(self.image, self.image_size)
        self.image = pygame.transform.rotozoom(self.image, self.image_radius, self.image_scale)

        self.rect = self.image.get_rect(center=(self.x, self.y))

    def shoot(self):
        self.game.bullet_group.add(
            Bullet(self.rect.topleft[0], self.rect.topleft[1], self.radius)
        )

    def move(self):
        rad_angle = math.radians(self.radius)
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
