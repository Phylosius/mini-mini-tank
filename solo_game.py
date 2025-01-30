import pygame

from game import Game
from objects.tank import Tank


class SoloGame(Game):
    def __init__(self):
        Game.__init__(self, "Mini Mini Tank Solo")

        self.player = Tank(self, 0, 0)
        self.player_group.add(self.player)

    def check_keyboard_press(self):
        if self.keys[pygame.K_UP]:
            self.player.move()
        if self.keys[pygame.K_LEFT]:
            self.player.rotate_left()
        if self.keys[pygame.K_RIGHT]:
            self.player.rotate_right()
        if self.keys[pygame.K_SPACE]:
            self.player.shoot()

    def update(self):
        super().update()
        self.check_keyboard_press()


if __name__ == "__main__":
    game = SoloGame()
    game.run()


