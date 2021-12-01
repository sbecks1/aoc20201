with open("inputs/day1.txt") as f:
    lines = f.readlines()
lines = [int(line.rstrip()) for line in lines]


def part1():
    increased: int = 0

    for i, n in enumerate(lines):
        try:
            if lines[i + 1] > n:
                increased += 1
        except IndexError:
            print(f"{increased} increases for pt 1.")


def part2():
    increased: int = 0

    for i, n in enumerate(lines):
        try:
            sum_a = n + lines[i + 1] + lines[i + 2]
            sum_b = lines[i + 1] + lines[i + 2] + lines[i + 3]
            if sum_b > sum_a:
                increased += 1
        except IndexError:
            print(f"{increased} increases for pt 2.")
            break


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
