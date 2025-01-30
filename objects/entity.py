
class Entity:
    def __init__(self):

        self.max_health = 100
        self.health = self.max_health
        self.is_alive = True

        self.x = 50
        self.y = 50

        self.speed = 0

    def on_out_of_health(self):
        self.is_alive = False

    def apply_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.on_out_of_health()