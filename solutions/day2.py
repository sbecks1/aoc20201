with open("inputs/day2.txt") as f:
    lines = f.readlines()

lines = [line.rstrip().split(" ") for line in lines]


def part1(input):
    h_pos: int = 0
    depth: int = 0

    for instr in input:
        dir: str = instr[0]
        units: int = int(instr[1])
        if dir == "down":
            depth += units
        if dir == "up":
            depth -= units
        if dir == "forward":
            h_pos += units

    return h_pos * depth


def part2(input):
    h_pos: int = 0
    depth: int = 0
    aim: int = 0

    for instr in input:
        dir: str = instr[0]
        units: int = int(instr[1])
        if dir == "down":
            aim += units
        if dir == "up":
            aim -= units
        if dir == "forward":
            h_pos += units
            depth += aim * units

    return h_pos * depth


def main():
    print(part1(lines))
    print(part2(lines))


if __name__ == "__main__":
    main()
