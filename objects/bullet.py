from objects.entity_sprite import EntitySprite


class Bullet(EntitySprite):
    def __init__(self, x, y, rotation):
        EntitySprite.__init__(self, x, y,
                              speed=10, rotation=rotation,
                              image_path='sprites/bullet.png', image_radius=-90, image_size=(25, 25))

    def update(self):
        super().update()
        self.move()
