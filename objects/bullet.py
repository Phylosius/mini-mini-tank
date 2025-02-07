import pygame

from objects.entity_sprite import EntitySprite


class Bullet(EntitySprite):
    def __init__(self, shooter, x, y, rotation):
        EntitySprite.__init__(self, x, y,
                              speed=10, rotation=rotation,
                              image_path='sprites/bullet.png', image_radius=-90, image_size=(25, 25))

        self.damage = 10
        self.shooter = shooter

    def handle_player_collision(self, _player):
        self.hint(_player)
        self.kill()

    def check_players_collision(self):
        for player in pygame.sprite.spritecollide(self, self.shooter.game.player_group, False, pygame.sprite.collide_mask):
            if player != self.shooter:
                self.handle_player_collision(player)

    def update(self):
        super().update()
        self.check_players_collision()
        self.move()

    def hint(self, entity):
        entity.apply_damage(self.damage)
