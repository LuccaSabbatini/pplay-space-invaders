from src.pplay.sprite import Sprite
import src.classes.Laser
import src.classes.Shield


class Player:
    absolute_speed = 400
    move_leftKeybind = "LEFT"
    move_rightKeybind = "RIGHT"
    shootLaserKeybind = "SPACE"
    shotSpeed = 600

    def __init__(self, window, keyboard):
        self.window = window
        self.keyboard = keyboard
        self.game_object = Sprite("./assets/images/player.png", 1)

        self.shot_cooldown_absolute = 0.6
        self.shot_cooldown = 0
        self.shots = []

        self.game_object.x = (self.window.width / 2) - \
            (self.game_object.width / 2)
        self.game_object.y = (self.window.height) - \
            (self.game_object.height) - 20

        self.lives = 3
        self.shield = src.classes.Shield.Shield(self.window, self)

        self.absolute_speed = self.absolute_speed
        self.x_speed = self.absolute_speed

    def control(self):
        if (self.keyboard.key_pressed(self.shootLaserKeybind) and (self.shot_cooldown == 0)):
            self.shoot()

        if (self.keyboard.key_pressed(self.move_leftKeybind) and self.game_object.x > 0):
            self.move_left()

        if (self.keyboard.key_pressed(self.move_rightKeybind) and
                self.game_object.x < (self.window.width - self.game_object.width)):
            self.move_right()

    def move_left(self):
        self.game_object.x -= self.x_speed * self.window.delta_time()
        self.game_object.x = max(self.game_object.x, 20)

        self.shield.game_object.x -= self.x_speed * self.window.delta_time()
        self.shield.game_object.x = max(self.shield.game_object.x, 20)

    def move_right(self):
        self.game_object.x += self.x_speed * self.window.delta_time()
        self.game_object.x = min(
            self.game_object.x, self.window.width - self.game_object.width - 20)

        self.shield.game_object.x += self.x_speed * self.window.delta_time()
        self.shield.game_object.x = min(
            self.shield.game_object.x, self.window.width - self.game_object.width - 20)

    def shoot(self):
        self.shot_cooldown = self.shot_cooldown_absolute
        self.shots.append(src.classes.Laser.Laser(
            self.window, self.shotSpeed, self, "red"))

    def shot_cooldown_check(self, time_passed):
        self.shot_cooldown -= time_passed
        self.shot_cooldown = max(self.shot_cooldown, 0)

    def take_hit(self):
        self.lives -= 1

        if self.lives == 0:
            self.window.game_over = True

    def respawn(self):
        self.game_object.x = (self.window.width / 2) - \
            (self.game_object.width / 2)
        self.game_object.y = (self.window.height) - \
            (self.game_object.height) - 20

        self.shield.game_object.x = (self.window.width / 2) - \
            (self.shield.game_object.width / 2)
        self.shield.game_object.y = (self.window.height) - \
            (self.shield.game_object.height) - 20

        self.shield.active = True
        self.shield.shield_cooldown = self.shield.shield_cooldown_absolute
