from objects.bullet import Bullet
from objects.entity_sprite import EntitySprite


class Tank(EntitySprite):

    def __init__(self, _game, x, y):
        EntitySprite.__init__(self, x, y,
                              rotation_speed=5,
                              image_path='sprites/tank.png', image_size=(50, 50), image_radius=-90)

        self.game = _game

    def shoot(self):
        self.game.bullet_group.add(
            Bullet(self.x, self.y, self.radius)
        )

    def rotate_left(self):
        self.radius += self.rotation_speed
        self.radius %= 360  # Garde l'angle dans les bornes [0, 360]

    def rotate_right(self):
        self.radius -= self.rotation_speed
        self.radius %= 360  # Garde l'angle dans les bornes [0, 360]
