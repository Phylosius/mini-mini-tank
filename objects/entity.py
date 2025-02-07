import math


class Entity:
    def __init__(self):

        self.max_health = 100
        self.health = self.max_health
        self.is_alive = True

        self.x = 50
        self.y = 50

        self.speed = 0

    def get_hint_angle(self, _entity, deg=True):
        rad_angle = math.atan2(self.y - _entity.y, _entity.x - self.x)
        return math.degrees(rad_angle) if deg else rad_angle

    def get_distance(self, _entity):
        return math.sqrt(abs(self.x - _entity.x) + abs(_entity.y - self.y))

    def on_out_of_health(self):
        self.is_alive = False

    def apply_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.on_out_of_health()