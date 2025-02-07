import pygame.time

from objects.tank import Tank


class AutoTank(Tank):
    def __init__(self, _game, x, y):
        super().__init__(_game, x, y)
        self.speed = 2

    def follow_and_shoot_player(self, orbit=15, shoot_delay=500):
        """
        Make the Tank follow and shoot the player in solo game

        :param int orbit: min distance between the player and the Tank
        :param int shoot_delay: delay between each shoot
        :return: None
        """
        target = self.game.player
        self.radius = self.get_hint_angle(target)

        if pygame.time.get_ticks() % shoot_delay == 0:
            self.shoot()

        if self.get_distance(target) > orbit:
            self.move()

    def update(self):
        super().update()
        self.follow_and_shoot_player()
