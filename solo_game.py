import pygame

from game import Game
from objects.tank import Tank
from services.player_controller import PlayerController, KeyBinder


class SoloGame(Game):
    def __init__(self):
        Game.__init__(self, "Mini Mini Tank Solo")

        self.player = Tank(self, 0, 0)
        self.player_group.add(self.player)

        self.player_binder = KeyBinder(self.player,
                                       pygame.K_q, pygame.K_d,
                                       pygame.K_z, pygame.K_s,
                                       pygame.K_LSHIFT)
        self.player_controller = PlayerController([self.player_binder])

    def handle_pygame_event(self, event):

        # for action to be performed once after pressing
        if event.type == pygame.KEYDOWN:
            self.player_controller.handle_player_shooting(event)

    def update(self):
        super().update()
        self.player_controller.update_player_position(self.keys)


if __name__ == "__main__":
    game = SoloGame()
    game.run()


