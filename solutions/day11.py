from dataclasses import dataclass

with open("inputs/day11.txt") as f:
    data = [[int(octo) for octo in list(line.strip())] for line in f.readlines()]


@dataclass
class Dumbo:
    energy: int
    row: int
    col: int
    flashed: bool = False

    def try_flash(self):
        if self.energy > 9 and not self.flashed:
            self.flashed = True

    def reset(self):
        self.energy = 0
        self.flashed = False

    def get_neighbor_positions(self):

        up = (self.row - 1, self.col)
        up_right = (self.row - 1, self.col + 1)
        up_left = (self.row - 1, self.col - 1)
        left = (self.row, self.col - 1)
        down_left = (self.row + 1, self.col - 1)
        down = (self.row + 1, self.col)
        right = (self.row, self.col + 1)
        down_right = (self.row + 1, self.col + 1)

        return [
            pos
            for pos in [up, up_right, up_left, left, down_left, down, right, down_right]
            if -1 not in pos and 10 not in pos
        ]


class DumboGrid:
    def __init__(self, init_state: list[list[Dumbo]]):
        self.state = init_state
        self.step_num = 0
        self.total_flashes = 0
        self.new_flashers: list[Dumbo] = []
        self.flashed_on_step: list[Dumbo] = []
        self.step_complete = False
        self.simulaneous_flashes = []

    def do_step(self):
        self.step_num += 1
        for row in self.state:
            for octo in row:
                octo.energy += 1

        while not self.step_complete:
            self.flash_check()

        for octo in self.flashed_on_step:
            octo.reset()

        if len(self.flashed_on_step) == (len(self.state) * len(self.state[0])):
            self.simulaneous_flashes.append(self.step_num)

        self.flashed_on_step = []
        self.step_complete = False

    def flash_check(self):
        for row in self.state:
            for octo in row:
                octo.try_flash()
                if octo.flashed and octo not in self.flashed_on_step:
                    self.new_flashers.append(octo)

        self.propagate_flash()

    def propagate_flash(self):

        if len(self.new_flashers) == 0:
            self.step_complete = True

        for octo in self.new_flashers:
            self.total_flashes += 1

            for pos in octo.get_neighbor_positions():
                row = pos[0]
                col = pos[1]
                self.state[row][col].energy += 1

            self.flashed_on_step.append(octo)

        self.new_flashers = []


def parse_input(input):
    grid = [[] for i in range(len(input))]
    for ridx, row in enumerate(input):
        for cidx, col in enumerate(row):
            grid[ridx].append(Dumbo(col, ridx, cidx))
    return grid


dumbos = parse_input(data)
dumbo_grid = DumboGrid(dumbos)


def part1():
    while dumbo_grid.step_num < 100:
        dumbo_grid.do_step()

    print(dumbo_grid.total_flashes)


def part2():
    while len(dumbo_grid.simulaneous_flashes) == 0:
        dumbo_grid.do_step()

    print(dumbo_grid.simulaneous_flashes[0])


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
