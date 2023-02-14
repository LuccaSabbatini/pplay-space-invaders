from src.pplay.sprite import Sprite


class Monster:
    base_speed = 30
    orientation = True

    def __init__(self, window, monster_index, x_position, y_position):
        self.window = window
        self.monster_index = monster_index
        self.game_object = Sprite("./assets/images/enemy_ship.png", 1)

        self.game_object.x = x_position
        self.game_object.y = y_position

        self.monster_speed = self.base_speed * self.window.game_difficulty
        self.x_speed = self.monster_speed
        self.y_speed = self.game_object.height

    def move_down(self):
        self.game_object.y += self.y_speed

        if self.game_object.y < self.window.height:
            return False

        return True

    def move_left(self, orientation):
        self.game_object.x -= self.x_speed * self.window.delta_time()
        if self.game_object.x < 0:
            self.game_object.x = 0
            return not orientation
        return orientation

    def move_right(self, orientation):
        self.game_object.x += self.x_speed * self.window.delta_time()
        if self.game_object.x > self.window.width - self.game_object.width:
            self.game_object.x = self.window.width - self.game_object.width
            return not orientation
        return orientation

    def move(self, orientation):
        return self.move_right(orientation) if orientation else self.move_left(orientation)
