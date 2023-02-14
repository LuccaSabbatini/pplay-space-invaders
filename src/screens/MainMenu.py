import sys
import src.components.Button
import src.screens.Game
import src.screens.Difficulty
import src.screens.Ranking


class MainMenu:
    def __init__(self, window, mouse, keyboard):
        self.window = window
        self.mouse = mouse
        self.keyboard = keyboard
        self.screen = self

        self.title = src.pplay.sprite.Sprite(
            "./assets/images/space_invaders_logo.png")

        self.play_button = src.components.Button.Button(
            "./assets/images/play_button.png", 0, 0)
        self.difficulty_button = src.components.Button.Button(
            "./assets/images/difficulty_button.png", 0, 0)
        self.ranking_button = src.components.Button.Button(
            "./assets/images/ranking_button.png", 0, 0)
        self.exit_button = src.components.Button.Button(
            "./assets/images/exit_button.png", 0, 0)

        self.title.x = (self.window.width / 2) - self.title.width / 2
        self.title.y = 50

        self.play_button.game_object.x = (
            self.window.width / 2) - self.play_button.game_object.width / 2
        self.play_button.game_object.y = 200

        self.difficulty_button.game_object.x = (
            self.window.width / 2) - self.difficulty_button.game_object.width / 2
        self.difficulty_button.game_object.y = 300

        self.ranking_button.game_object.x = (
            self.window.width / 2) - self.ranking_button.game_object.width / 2
        self.ranking_button.game_object.y = 400

        self.exit_button.game_object.x = (
            self.window.width / 2) - self.exit_button.game_object.width / 2
        self.exit_button.game_object.y = 500

    def draw_screen(self):
        self.title.draw()
        self.play_button.game_object.draw()
        self.difficulty_button.game_object.draw()
        self.ranking_button.game_object.draw()
        self.exit_button.game_object.draw()

    def loop(self, click):
        self.draw_screen()

        if (self.mouse.is_over_object(self.play_button.game_object) and click):
            self.screen = src.screens.Game.Game(
                self.window, self.mouse, self.keyboard)

        if (self.mouse.is_over_object(self.difficulty_button.game_object) and click):
            self.screen = src.screens.Difficulty.Difficulty(
                self.window, self.mouse, self.keyboard)

        if (self.mouse.is_over_object(self.ranking_button.game_object) and click):
            self.screen = src.screens.Ranking.Ranking(
                self.window, self.mouse, self.keyboard)

        if (self.mouse.is_over_object(self.exit_button.game_object) and click):
            sys.exit()
