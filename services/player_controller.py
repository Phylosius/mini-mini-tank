import pygame


class PlayerController:
    def __init__(self, player, keys):
        self.player = player
        self.keys = keys

    def handle_player_shooting(self, event):
        if event.key == pygame.K_SPACE:
            self.player.shoot()

    def check_keyboard_press(self):
        # for action to be performed while pressing
        if self.keys[pygame.K_UP]:
            self.player.move()
        elif self.keys[pygame.K_DOWN]:
            self.player.move(-1)
        if self.keys[pygame.K_LEFT]:
            self.player.rotate_left()
        if self.keys[pygame.K_RIGHT]:
            self.player.rotate_right()

    def update_player_position(self):
        self.check_keyboard_press()
        self.player.fix_state()

