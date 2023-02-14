from src.pplay.sprite import Sprite


class Laser:
    def __init__(self, window, initial_speed, shooter, color):
        self.window = window
        self.shooter = shooter
        self.game_object = Sprite(
            f"./assets/images/laser_{color}.png", 1)

        offset = -self.game_object.height if color == "red" else +self.game_object.height

        self.game_object.x = self.shooter.game_object.x + \
            (self.shooter.game_object.width / 2) - self.game_object.width / 2
        self.game_object.y = self.shooter.game_object.y + offset

        self.absolute_speed = initial_speed
        self.x_speed = self.absolute_speed
        self.y_speed = self.absolute_speed

    def move_up(self):
        self.game_object.y -= self.y_speed * self.window.delta_time()

        return self.game_object.y > 0

    def move_down(self):
        self.game_object.y += self.y_speed * self.window.delta_time()

        return self.game_object.y < self.window.height
