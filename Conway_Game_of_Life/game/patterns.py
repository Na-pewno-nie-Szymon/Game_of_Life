from dataclasses import dataclass
import collections
from pathlib import Path

PATTERNS_FILE = Path(__file__).parent / "patterns.toml"

try:
    import tomllib
except:
    # for python version lower than 3.11
    import tomli as tomlib

'''
Steps done: 1 and 2
'''

ALIVE = "♥"
DEAD = "‧"

@dataclass
class Pattern:
    name: str
    alive_cells: set[tuple[int, int]]

    @classmethod
    def from_toml(cls, name, toml_data):
        return cls(
            name,
            alive_cells = {tuple(cell) for cell in toml_data["alive_cells"]}
        )

class LifeGrid:
    def __init__(self, pattern):
        self.pattern = pattern

    def evolve(self):
        neighbors = (
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 0),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, -1)
        )

        num_neighbors = collections.defaultdict(int)

        for row, col, in self.pattern.alive_cells:
            for drow, dcol in neighbors:
                num_neighbors[(row + drow, col + dcol)] += 1

        stay_alive = {
            cell for cell, num in num_neighbors.items() if num in {2, 3}
        } & self.pattern.alive_cells

        come_alive = {
            cell for cell, num in num_neighbors.items() if num == 3
        } - self.pattern.alive_cells

        self.pattern.alive_cells = stay_alive | come_alive

    def as_string(self, bbox):
        start_col, start_row, end_col, end_row = bbox

        display = [self.pattern.name.center(2* (end_col - start_col))]

        for row in range(start_row, end_row):
            display_row = [
                ALIVE if (row, col) in self.pattern.alive_cells else DEAD
                for col in range(start_col, end_col)
            ]
            display.append(" ".join(display_row))
        return '\n'.join(display)

    def __str__(self):
        return (
            f'{self.pattern.name}:\n'
            f'Alive cells -> {sorted(self.pattern.alive_cells)}'
        )
    
def get_pattern(name, filename=PATTERNS_FILE):
    data = tomllib.loads(filename.read_text(encoding='utf=8'))
    return Pattern.from_toml(name, toml_data=data[name])

def get_all_patterns(filename=PATTERNS_FILE):
    data = tomllib.loads(filename.read_text(encoding='utf-8'))
    return [
        Pattern.from_toml(name, toml_data) for name, toml_data in data.items()
    ]