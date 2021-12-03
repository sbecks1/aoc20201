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
    def comm_char_at_bin_pos(input: "list[str]", bin_pos: int) -> str:
        bin_positions = list(zip(*input))
        if bin_positions[bin_pos].count("1") >= len(input) / 2:
            return "1"
        else:
            return "0"

    o2 = input.copy()
    co2 = input.copy()
    for i in range(len(input[0])):
        if len(o2) > 1:
            o2 = [n for n in o2 if n[i] == comm_char_at_bin_pos(o2, i)]
        else:
            break

    for i in range(len(input[0])):
        if len(co2) > 1:
            co2 = [n for n in co2 if n[i] != comm_char_at_bin_pos(co2, i)]
        else:
            break

    return int("0b" + o2[0], 2) * int("0b" + co2[0], 2)


def main():
    print(part1(lines))
    print(part2(lines))


if __name__ == "__main__":
    main()
