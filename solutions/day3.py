with open("inputs/day3.txt") as f:
    lines = [line.rstrip() for line in f.readlines()]


def part1(input: "list[str]") -> int:
    gamma = "0b"
    epsilon = "0b"
    for i in zip(*input):
        if i.count("1") > len(i) / 2:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"

    return int(gamma, 2) * int(epsilon, 2)


def part2(input: "list[str]") -> int:
    pass


def main():
    print(part1(lines))


if __name__ == "__main__":
    main()
