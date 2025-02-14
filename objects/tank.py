import math

import pygame

from objects.bullet import Bullet
from objects.entity_sprite import EntitySprite


class Tank(EntitySprite):

    def __init__(self, _game, x, y):
        EntitySprite.__init__(self, x, y,
                              rotation_speed=5,
                              image_path='sprites/tank.png', image_size=(50, 50), image_radius=-90)

        self.game = _game
        self.last_position = (self.x, self.y)
        self.last_rotation = self.radius
        self.last_image = self.image

    def rotate_right(self):
        super().rotate_right()

    def rotate_left(self):
        super().rotate_left()

    def move(self, direction=1):
        super().move(direction)

    def is_collide_mask(self, other):
        return pygame.sprite.spritecollide(self, other, False, pygame.sprite.collide_mask)

    def is_collide(self, other):
        return pygame.sprite.spritecollide(self, other, False)

    def fix_state(self):
        player_group = self.game.player_group.copy()
        player_group.remove(self)
        if self.is_collide_mask(player_group):
            self.x, self.y = self.last_position
            self.radius = self.last_rotation
            self.image = self.last_image

    def cache_state(self):
        player_group = self.game.player_group.copy()
        player_group.remove(self)
        if not self.is_collide(player_group):
            self.last_position = (self.x, self.y)
            self.last_rotation = self.radius
            self.last_image = self.image

    def update(self):
        self.cache_state()
        super().update()
        # if not self.is_alive:
        #     self.kill()

    def shoot(self):
        self.game.bullet_group.add(
            Bullet(self,
                   self.x + 6 * math.cos(math.radians(self.radius)),
                   self.y - 6 * math.sin(math.radians(self.radius)),
                   self.radius)
        )

