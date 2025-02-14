import pygame

from game import Game
from objects.tank import Tank
from objects.auto_tank import AutoTank
from services.player_controller import PlayerController


class SoloGame(Game, PlayerController):
    def __init__(self):
        Game.__init__(self, "Mini Mini Tank Solo")

        self.player = Tank(self, 0, 0)
        self.player_group.add(self.player)

        PlayerController.__init__(self, self.player, self.keys)

    def handle_pygame_event(self, event):

        # for action to be performed once after pressing
        if event.type == pygame.KEYDOWN:
            self.handle_player_shooting(event)

    def update(self):
        super().update()
        self.update_player_position()


if __name__ == "__main__":
    game = SoloGame()
    game.run()


