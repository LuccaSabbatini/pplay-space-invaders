class HUD:
    def __init__(self, window, player):
        self.window = window
        self.player = player

    def draw_hud(self):
        self.window.draw_text("Lives: " + str(self.player.lives),
                              10, 10, 20, (255, 255, 255), "Arial", True, False)
        self.window.draw_text("Level: " + str(int(((self.window.game_difficulty - 3) / 0.5) + 1)),
                              self.window.width - 90, 10, 20, (255, 255, 255), "Arial", True, False)
