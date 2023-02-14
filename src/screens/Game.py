import time
import random
import src.pplay.sprite
import src.components.Button
import src.classes.Player
import src.classes.MonsterGrid
import src.screens.MainMenu
import src.components.Score
import src.components.HUD


class Game:
    reset = False

    def __init__(self, window, mouse, keyboard):
        self.window = window
        self.mouse = mouse
        self.keyboard = keyboard
        self.screen = self
        self.player = src.classes.Player.Player(window, keyboard)
        self.score = src.components.Score.Score(self.window)
        self.hud = src.components.HUD.HUD(self.window, self.player)
        self.monster_grid = src.classes.MonsterGrid.MonsterGrid(
            self.window, self.score)

        self.game_over_title = src.pplay.sprite.Sprite(
            "./assets/images/game_over_title.png")
        self.game_over_title.x = (
            self.window.width / 2) - (self.game_over_title.width / 2)
        self.game_over_title.y = (self.window.height / 2) - \
            (self.game_over_title.height / 2)

    def draw_screen(self):
        self.score.draw_score()
        self.hud.draw_hud()
        self.player.game_object.draw()

        if self.player.shield.active:
            self.player.shield.game_object.draw()

        # Loop through player shots
        for shot in self.player.shots:
            # Draw shots
            shot.game_object.draw()

            # Move shots
            is_in_bounds = shot.move_up()

            # Check with shot is in bounds
            if not is_in_bounds:
                self.player.shots.remove(shot)
                del shot

                continue

    def loop(self, click):
        #  Draw screen elements
        self.draw_screen()

        # Loop through monsters
        for shot in self.monster_grid.shots:
            # Draw shots
            shot.game_object.draw()

            # Move shots
            is_in_bounds = shot.move_down()

            # Check with shot is in bounds
            if not is_in_bounds:
                self.monster_grid.shots.remove(shot)
                del shot

                continue

            # Check collisions with player
            if shot.game_object.collided(self.player.game_object):
                if not self.player.shield.active:
                    self.player.take_hit()
                    self.player.respawn()

                self.monster_grid.shots.remove(shot)
                del shot

        # Loop through all monsters
        counter = 0

        # Get number of alive monsters
        alive_monsters = self.monster_grid.get_alive_monsters_count()

        # Select a random iteration of monsters to decide which one will shoot at the player
        random_monster_iteration = random.randint(
            0, alive_monsters - 1) if alive_monsters > 1 else 0

        for row in self.monster_grid.monster_rows:
            for monster in row.monsters:
                if counter == random_monster_iteration:
                    self.selected_monster = monster

                # Draw Monsters
                monster.game_object.draw()
                new_orientation = monster.move(self.monster_grid.orientation)
                if new_orientation != self.monster_grid.orientation:
                    self.monster_grid.orientation = new_orientation
                    self.monster_grid.move_rows_down(self.player.game_object.y)

                # Loop through player shots
                for shot in self.player.shots:
                    # Check collisions with monsters
                    if shot.game_object.collided(monster.game_object):
                        self.score.count_points()

                        row.monsters.remove(monster)
                        del monster

                        self.player.shots.remove(shot)
                        del shot

                # Increment count
                counter += 1

        # Player Commands
        self.player.shield.shield_cooldown_check(self.window.delta_time())
        self.player.shot_cooldown_check(self.window.delta_time())
        self.player.control()

        # Monsters Commands
        self.monster_grid.shot_cooldown_check(self.window.delta_time())
        if self.monster_grid.shot_cooldown == 0:
            self.monster_grid.shoot(self.selected_monster)

        # New Level
        if (not self.window.game_over and (self.monster_grid.get_alive_monsters_count() == 0)):
            self.monster_grid.monster_rows = []
            self.window.game_difficulty += 0.5
            self.monster_grid = src.classes.MonsterGrid.MonsterGrid(
                self.window, self.score)

        # Return to menu
        if self.keyboard.key_pressed("ESC"):
            self.monster_grid = None
            self.screen = src.screens.MainMenu.MainMenu(
                self.window, self.mouse, self.keyboard)

        # Game Over
        if (self.window.game_over):
            self.game_over_title.draw()

            player_name = input("Enter your name: ")

            self.window.ranking.append(
                {"name": player_name, "points": self.score.score})

            sorted_ranking = sorted(self.window.ranking,
                                    key=lambda entry: entry["points"], reverse=True)

            self.window.ranking = sorted_ranking

            self.window.game_over = False
            self.monster_grid = None
            self.screen = src.screens.MainMenu.MainMenu(
                self.window, self.mouse, self.keyboard)
