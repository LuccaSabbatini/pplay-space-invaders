import math
import src.classes.Monster


class MonsterRow:
    def __init__(self, window, row_index, y_position, row_parity):
        self.window = window
        self.y_position = y_position
        self.monsters = []
        self.row_index = row_index

        # Represents twice of the monster count
        monsters_count = math.floor((self.window.width) / 98)
        monster_space = self.window.width / monsters_count
        monster_index = 0

        for i in range(monsters_count):
            if ((i == monsters_count - 1 and row_parity == 1) or i == monsters_count - 1 or i == 0):
                continue
            if i % 2 == row_parity:
                self.monsters.append(src.classes.Monster.Monster(
                    self.window, monster_index, ((i + 1) * monster_space - 49), y_position))
                monster_index += 1

    def move_down(self, player_y):
        for monster in self.monsters:
            monster.move_down()

            if monster.game_object.y + monster.game_object.height >= player_y:
                self.window.game_over = True
                return
