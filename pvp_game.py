import pygame

from objects.tank import Tank
from services.player_controller import KeyBinder
from solo_game import SoloGame


class PvpGame(SoloGame):
    def __init__(self):
        super().__init__()
        self.player2 = Tank(self, 500, 500)
        self.player2_binder = KeyBinder(self.player2,
                                        pygame.K_LEFT, pygame.K_RIGHT,
                                        pygame.K_UP, pygame.K_DOWN,
                                        pygame.K_SPACE)

        self.player_group.add(self.player2)
        self.player_controller.players_binders.append(self.player2_binder)


if __name__ == '__main__':
    game = PvpGame()
    game.run()
