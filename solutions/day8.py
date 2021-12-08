with open("inputs/day8.txt") as f:
    output_val = [line.split("|")[1].strip() for line in f.readlines()]


def part1(vals) -> int:
    lengths_1478 = [2, 4, 3, 7]

    known_digits = 0

    for line in output_val:
        for digit in line.split(" "):
            if len(digit) in lengths_1478:
                known_digits += 1

    return known_digits


def main():
    print(part1(output_val))


if __name__ == "__main__":
    main()
