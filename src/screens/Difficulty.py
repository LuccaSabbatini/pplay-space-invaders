import src.components.Button
import src.screens.MainMenu
import src.pplay.sprite


class Difficulty:
    def __init__(self, window, mouse, keyboard):
        self.window = window
        self.mouse = mouse
        self.keyboard = keyboard
        self.screen = self

        self.title = src.pplay.sprite.Sprite(
            "./assets/images/difficulty_title.png")

        self.easy_button = src.components.Button.Button(
            "./assets/images/difficulty_easy.png", 0, 0)
        self.normal_button = src.components.Button.Button(
            "./assets/images/difficulty_normal.png", 0, 0)
        self.hard_button = src.components.Button.Button(
            "./assets/images/difficulty_hard.png", 0, 0)

        self.title.x = (self.window.width / 2) - self.title.width / 2
        self.title.y = 50

        self.easy_button.game_object.x = (
            self.window.width / 2) - self.easy_button.game_object.width / 2
        self.easy_button.game_object.y = 200

        self.normal_button.game_object.x = (
            self.window.width / 2) - self.normal_button.game_object.width / 2
        self.normal_button.game_object.y = 300

        self.hard_button.game_object.x = (
            self.window.width / 2) - self.hard_button.game_object.width / 2
        self.hard_button.game_object.y = 400

    def draw_screen(self):
        self.title.draw()
        self.easy_button.game_object.draw()
        self.normal_button.game_object.draw()
        self.hard_button.game_object.draw()

    def loop(self, click):
        self.draw_screen()

        if (self.mouse.is_over_object(self.easy_button.game_object) and click):
            self.window.game_difficulty = 1
            self.screen = src.screens.MainMenu.MainMenu(
                self.window, self.mouse, self.keyboard)

        if (self.mouse.is_over_object(self.normal_button.game_object) and click):
            self.window.game_difficulty = 3
            self.screen = src.screens.MainMenu.MainMenu(
                self.window, self.mouse, self.keyboard)

        if (self.mouse.is_over_object(self.hard_button.game_object) and click):
            self.window.game_difficulty = 5
            self.screen = src.screens.MainMenu.MainMenu(
                self.window, self.mouse, self.keyboard)

        if self.keyboard.key_pressed("ESC"):
            self.screen = src.screens.MainMenu.MainMenu(
                self.window, self.mouse, self.keyboard)
