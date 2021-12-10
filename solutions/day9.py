from typing import Optional
import functools


with open("inputs/day9.txt") as f:
    grid = [list(map(int, line.strip())) for line in f.readlines()]


def is_sink(cell_val: int, cell_y: int, cell_x: int) -> bool:
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


def get_neighbors(cell_y: int, cell_x: int):
    # cell[y][x]
    neighbors: dict[str, Optional[dict]] = {
        "up": None,
        "down": None,
        "left": None,
        "right": None,
    }

    if cell_y != 0:
        neighbors["up"] = {
            "val": grid[cell_y - 1][cell_x],
            "yx": (cell_y - 1, cell_x),
        }

    try:
        neighbors["down"] = {
            "val": grid[cell_y + 1][cell_x],
            "yx": (cell_y + 1, cell_x),
        }
    except IndexError:
        pass

    if cell_x != 0:
        neighbors["left"] = {
            "val": grid[cell_y][cell_x - 1],
            "yx": (cell_y, cell_x - 1),
        }

    try:
        neighbors["right"] = {
            "val": grid[cell_y][cell_x + 1],
            "yx": (cell_y, cell_x + 1),
        }
    except IndexError:
        pass

    return [
        neighbors[key]["yx"]
        for key in neighbors
        if neighbors[key] is not None and neighbors[key]["val"] != 9
    ]


def export_esri_ascii(filepath: str):
    """Writing output to ASCII raster format"""
    with open(filepath, "w") as asc:
        asc.write(f"NCOLS {len(grid)}\n")
        asc.write(f"NROWS {len(grid[0])}\n")
        asc.write("XLLCORNER 0\n")
        asc.write("YLLCORNER 0\n")
        asc.write("CELLSIZE 30\n")
        asc.write("NODATA_VALUE -999\n")
        for row in grid:
            asc.write(" ".join([str(n) for n in row]) + "\n")


def fill_basin(cell_y: int, cell_x: int):
    current_basin: list[tuple] = [(cell_y, cell_x)]  # starting from sink
    i = 0
    while i < len(current_basin):
        new_neighbors = get_neighbors(current_basin[i][0], current_basin[i][1])
        for neighbor in new_neighbors:
            if neighbor not in current_basin:
                current_basin.append(neighbor)
        i += 1
    return current_basin


def part1() -> int:
    risk_sum = 0

    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            if is_sink(val, y, x):
                risk_sum += val + 1

    return risk_sum


def part2():

    basins = []
    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            if is_sink(val, y, x):
                new_basin = fill_basin(y, x)
                basins.append(new_basin)
    large_basins = sorted([len(basin) for basin in basins], reverse=True)[:3]
    product = lambda x, y: x * y
    return functools.reduce(product, large_basins)


def main():
    print(part1())
    print(part2())
    export_esri_ascii("visualizations/day9pt1.asc")  # just for fun


if __name__ == "__main__":
    main()
