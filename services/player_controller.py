import pygame


class KeyBinder:
    def __init__(self,
                 player,
                 rotate_left, rotate_right,
                 move_forward, move_backward,
                 shoot):

        self.player = player
        self.rotate_left = rotate_left
        self.rotate_right = rotate_right
        self.move_forward = move_forward
        self.move_backward = move_backward
        self.shoot = shoot

    def check_shooting(self, event):
        if event.key == self.shoot:
            self.player.shoot()

    def check_keyboard_press(self, keys):
        # for action to be performed while pressing
        if keys[self.move_forward]:
            self.player.move()
        elif keys[self.move_backward]:
            self.player.move(-1)
        if keys[self.rotate_left]:
            self.player.rotate_left()
        if keys[self.rotate_right]:
            self.player.rotate_right()



class PlayerController:
    def __init__(self, key_binders):
        self.players_binders = key_binders
        self.players = []

    def init(self):
        self.players = list(map(lambda b: b.player, self.players_binders))

    def handle_player_shooting(self, event):
        for biding in self.players_binders:
            biding.check_shooting(event)

    def check_keyboard_press(self, keys):
        for biding in self.players_binders:
            biding.check_keyboard_press(keys)

    def update_player_position(self, keys):
        self.check_keyboard_press(keys)
        for player in self.players:
            player.fix_state()

