from src.pplay.sprite import *


class Button:
    def __init__(self, assetPath, x_position, y_position):
        self.game_object = Sprite(assetPath, 1)
        self.game_object.x = x_position
        self.game_object.y = y_position
