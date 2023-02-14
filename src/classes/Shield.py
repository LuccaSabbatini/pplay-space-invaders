from src.pplay.sprite import Sprite


class Shield:
    def __init__(self, window, player):
        self.window = window
        self.player = player
        self.game_object = Sprite("./assets/images/shield.png", 1)

        self.game_object.x = (self.window.width / 2) - \
            (self.game_object.width / 2)
        self.game_object.y = (self.window.height) - \
            (self.game_object.height) - 20

        self.active = False

        self.shield_cooldown_absolute = 2
        self.shield_cooldown = 0

    def shield_cooldown_check(self, time_passed):
        self.shield_cooldown -= time_passed
        self.shield_cooldown = max(self.shield_cooldown, 0)

        if self.shield_cooldown == 0:
            self.active = False
