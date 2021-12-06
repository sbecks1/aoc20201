from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


@dataclass
class Line:
    geometry: list[Point]

    def is_vertical(self) -> bool:
        return len({pt.x for pt in self.geometry}) == 1

    def is_horizontal(self) -> bool:
        return len({pt.y for pt in self.geometry}) == 1


class MapGrid:
    def __init__(self, x_max: int, y_max: int):
        self.grid: list[list] = self.create_grid(x_max, y_max)
        self.layers: list[Line] = []

    def create_grid(self, x_max, y_max):
        return [[0 for i in range(0, x_max + 1)] for i in range(0, y_max + 1)]

    def add_line(self, line: Line):
        for pt in line.geometry:
            self.grid[pt.y][pt.x] += 1

        if line.is_vertical():
            y_coords = [pt.y for pt in line.geometry]
            for i in range(min(y_coords) + 1, max(y_coords) + 1):
                self.grid[i][line.geometry[0].x] += 1

        if line.is_horizontal():
            x_coords = [pt.x for pt in line.geometry]
            for i in range(min(x_coords) + 1, max(x_coords) + 1):
                self.grid[line.geometry[0].y][i] += 1


def part1():
    pass


def main():
    with open("inputs/day5.txt") as f:
        for line in f.readlines():
            print(line)


if __name__ == "__main__":
    main()
