import objects.entity as entity
import pygame
import math

class EntitySprite(entity.Entity, pygame.sprite.Sprite):
    def __init__(self, x, y,
                 speed = 7, rotation_speed = 5,
                 rotation = 0, image_path = 'sprites/tank.png',
                 image_size = (50, 50), image_radius = -90, image_scale = 1):
        pygame.sprite.Sprite.__init__(self)
        entity.Entity.__init__(self)

        self.x = x
        self.y = y

        self.speed = speed
        self.rotation_speed = rotation_speed  # Plus petit pour des rotations plus fines
        self.radius = rotation

        self.image_path = image_path
        self.image_size = image_size
        self.image_radius = image_radius
        self.image_scale = image_scale

        self.image = pygame.image.load(self.image_path)
        self.image = pygame.transform.scale(self.image, self.image_size)
        self.image = pygame.transform.rotozoom(self.image, self.image_radius, self.image_scale)

        # self.image.set_at((self.image.get_rect().centerx, self.image.get_rect().centery), 'black')

        self.rect = self.image.get_rect(center=(self.x, self.y))

    def move(self):
        rad_angle = math.radians(self.radius)
        self.x += math.cos(rad_angle) * self.speed
        self.y -= math.sin(rad_angle) * self.speed  # Soustraction car l'axe y est inversé

    def draw(self, screen):
        rotated_image = pygame.transform.rotozoom(self.image, self.radius, 1)
        screen.blit(rotated_image, rotated_image.get_rect(center=(self.x, self.y)))

    def update(self):
        self.rect.topleft = (self.x, self.y)