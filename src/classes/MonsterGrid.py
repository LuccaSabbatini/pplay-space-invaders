import random
import src.classes.MonsterRow
import src.classes.Laser


class MonsterGrid:
    shot_speed = 600

    def __init__(self, window, score):
        self.window = window
        self.score = score
        self.monster_rows = []
        self.monsters_rows_count = 4

        orientation_randomness = random.randint(0, 10)
        self.orientation = orientation_randomness > 5

        self.shot_cooldown_absolute = max(
            1.5 - (0.1 * ((self.window.game_difficulty - 3) / 0.5)), 0.5)
        self.shot_cooldown = 0
        self.shots = []

        monster_space = 70
        row_parity = 0

        for i in range(self.monsters_rows_count):
            y_position = (i + 1) * monster_space + (self.window.height / 10)
            self.monster_rows.append(src.classes.MonsterRow.MonsterRow(
                self.window, i, y_position, row_parity))
            # row_parity = not row_parity  # If uncommented, monster alignment is alternated

    def shoot(self, random_monster):
        if self.shot_cooldown == 0:
            self.shot_cooldown = self.shot_cooldown_absolute

            self.shots.append(src.classes.Laser.Laser(
                self.window, self.shot_speed, random_monster, "green"))

    def shot_cooldown_check(self, time_passed):
        self.shot_cooldown -= time_passed
        self.shot_cooldown = max(self.shot_cooldown, 0)

    def get_alive_monsters_count(self):
        count = 0

        for row in self.monster_rows:
            count += len(row.monsters)

        return count

    def move_rows_down(self, player_y):
        for row in self.monster_rows:
            row.move_down(player_y)
