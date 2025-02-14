import math


class Entity:
    def __init__(self):

        self.max_health = 100
        self.health = self.max_health
        self.is_alive = True

        self.x = 50
        self.y = 50

        self.speed = 0
        self.radius = -90

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

    def rotate_left(self):
        self.radius += self.rotation_speed
        self.radius %= 360  # Garde l'angle dans les bornes [0, 360]

    def rotate_right(self):
        self.radius -= self.rotation_speed
        self.radius %= 360  # Garde l'angle dans les bornes [0, 360]

    def move(self, direction=1):
        rad_angle = math.radians(self.radius)
        self.x += math.cos(rad_angle) * self.speed * direction
        self.y -= math.sin(rad_angle) * self.speed * direction # Soustraction car l'axe y est inversé