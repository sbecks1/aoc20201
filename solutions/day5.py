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
        return [[0 for i in range(0, x_max + 2)] for i in range(0, y_max + 2)]

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


def parse_line_text(text: str) -> Line:
    pt1 = text.split(" -> ")[0]
    pt1_x = int(pt1.split(",")[0])
    pt1_y = int(pt1.split(",")[1])
    pt2 = text.split(" -> ")[1]
    pt2_x = int(pt2.split(",")[0])
    pt2_y = int(pt2.split(",")[1])

    return Line([Point(pt1_x, pt1_y), Point(pt2_x, pt2_y)])


def find_bottom_right(features: list[Line]) -> Point:
    x_max = 0
    y_max = 0

    for ft in features:
        big_x = max([pt.x for pt in ft.geometry])
        big_y = max([pt.x for pt in ft.geometry])
        if big_x > x_max:
            x_max = big_x
        if big_y > y_max:
            y_max = big_y

    return Point(x_max, y_max)


def part1():
    pass


def main():
    lines: list[Line] = []
    with open("inputs/day5.txt") as f:
        for line in f.readlines():
            line_ft = parse_line_text(line)
            if line_ft.is_horizontal() or line_ft.is_vertical():
                lines.append(line_ft)

    br_pt = find_bottom_right(lines)
    vent_map = MapGrid(br_pt.x, br_pt.y)
    for line in lines:
        vent_map.add_line(line)

    with open("inputs/map.txt", "w") as fo:
        for row in vent_map.grid:
            for coord in row:
                fo.write(str(coord))
            fo.write("\n")


if __name__ == "__main__":
    main()
