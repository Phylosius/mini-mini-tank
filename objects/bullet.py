import math

import pygame
from objects.entity import Entity


class Bullet(Entity):
    def __init__(self, x, y, angle):
        Entity.__init__(self)

        self.x = x
        self.y = y
        self.radius = angle
        self.speed = 10

        self.image_radius = -90
        self.image_size = (25, 25)
        self.image_path = 'sprites/bullet.png'

        self.image = pygame.image.load(self.image_path)
        self.image = pygame.transform.scale(self.image, self.image_size)
        self.image = pygame.transform.rotate(self.image, self.image_radius)
        self.image.fill('purple')
        self.rect = self.image.get_rect(center=(x, y))

    def move(self):
        rad_angle = math.radians(self.radius)
        self.x += self.speed * math.cos(rad_angle)
        self.y -= self.speed * math.sin(rad_angle)

    def draw(self, screen):
        rotated_image = pygame.transform.rotate(self.image, self.radius)
        rotated_rect = rotated_image.get_rect(center=(self.x, self.y))
        screen.blit(rotated_image, rotated_rect)

    def update(self):
        self.move()
        self.rect.topleft = (self.x, self.y)
