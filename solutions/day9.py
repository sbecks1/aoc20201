from typing import Optional


with open("inputs/day9.txt") as f:
    cells = [list(map(int, line.strip())) for line in f.readlines()]


def is_sink(grid, cell_val: int, cell_y: int, cell_x: int) -> bool:
    # cell[y][x]
    neighbors: dict[str, Optional[int]] = {
        "up": None,
        "down": None,
        "left": None,
        "right": None,
    }

    if cell_y != 0:
        neighbors["up"] = grid[cell_y - 1][cell_x]

    try:
        neighbors["down"] = grid[cell_y + 1][cell_x]
    except IndexError:
        pass

    if cell_x != 0:
        neighbors["left"] = grid[cell_y][cell_x - 1]

    try:
        neighbors["right"] = grid[cell_y][cell_x + 1]
    except IndexError:
        pass

    return all(
        [cell_val < val for val in neighbors.values() if val is not None]
    )  # burned by if 0 == False


def part1(grid) -> int:
    risk_sum = 0

    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            if is_sink(grid, val, y, x):
                risk_sum += val + 1

    return risk_sum


def main():
    print(part1(cells))


if __name__ == "__main__":
    main()
