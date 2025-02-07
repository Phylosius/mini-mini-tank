import math

from objects.bullet import Bullet
from objects.entity_sprite import EntitySprite


class Tank(EntitySprite):

    def __init__(self, _game, x, y):
        EntitySprite.__init__(self, x, y,
                              rotation_speed=5,
                              image_path='sprites/tank.png', image_size=(50, 50), image_radius=-90)

        self.game = _game

    def update(self):
        super().update()
        if not self.is_alive:
            self.kill()

    def shoot(self):
        self.game.bullet_group.add(
            Bullet(self,
                   self.x + 6 * math.cos(math.radians(self.radius)),
                   self.y - 6 * math.sin(math.radians(self.radius)),
                   self.radius)
        )

    def rotate_left(self):
        self.radius += self.rotation_speed
        self.radius %= 360  # Garde l'angle dans les bornes [0, 360]

    def rotate_right(self):
        self.radius -= self.rotation_speed
        self.radius %= 360  # Garde l'angle dans les bornes [0, 360]
