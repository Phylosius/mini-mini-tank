from objects.auto_tank import AutoTank
from solo_game import SoloDisplayedGame


class PvEGame(SoloDisplayedGame):
    def __init__(self):
        super().__init__()

    def init(self):
        if self.display:
            self.player_group.add(AutoTank(self, self.screen.get_width() // 2, self.screen.get_height() // 2))


if __name__ == '__main__':
    game = PvEGame()
    game.run()
