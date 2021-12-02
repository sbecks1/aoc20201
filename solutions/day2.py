with open("inputs/day2.txt") as f:
    lines = f.readlines()

lines = [line.rstrip().split(" ") for line in lines]


def part1(input):
    h_pos = 0
    depth = 0

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


def main():
    print(part1(lines))


if __name__ == "__main__":
    main()
