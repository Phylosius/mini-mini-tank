import pygame

from game import Game
from objects.tank import Tank


class SoloGame(Game):
    def __init__(self):
        Game.__init__(self, "Mini Mini Tank Solo")

        self.player = Tank(self, 0, 0)
        self.player_group.add(self.player)

    def handle_pygame_event(self, event):

        # for action to be performed once after pressing
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.player.shoot()

    def check_keyboard_press(self):
        # for action to be performed while pressing
        if self.keys[pygame.K_UP]:
            self.player.move()
        if self.keys[pygame.K_LEFT]:
            self.player.rotate_left()
        if self.keys[pygame.K_RIGHT]:
            self.player.rotate_right()

    def update(self):
        super().update()
        self.check_keyboard_press()


if __name__ == "__main__":
    game = SoloGame()
    game.run()


