with open("inputs/day6.txt") as f:
    ages = f.read().rstrip().split(",")

fishes: list[int] = [int(age) for age in ages]


def lifetime_reproduction(fish_age: int, num_steps: int) -> int:
    fish_count = 1
    age = fish_age
    for i in range(num_steps, 0, -1):
        if age == 0:
            age = 6
            fish_count += lifetime_reproduction(8, i - 1)
            continue
        age -= 1

    return fish_count


def count_per_day(initial_counts: dict[int, int], num_steps: int) -> int:
    age_counts = initial_counts
    while num_steps:
        next_day_counts = {i: 0 for i in range(9)}
        for age, count in age_counts.items():
            if age > 0:
                next_day_counts[age - 1] += count
            else:
                next_day_counts[6] += count
                next_day_counts[8] += count
        age_counts = next_day_counts.copy()
        num_steps -= 1

    return sum(age_counts.values())


def part1():

    total_fish = 0
    for fish in fishes:
        total_fish += lifetime_reproduction(fish, 80)
    print(total_fish)
    # per fish modelling wasn't the right choice, but leaving it in for posterity


def part2():
    first_scan = {i: fishes.count(i) for i in fishes}
    print(count_per_day(first_scan, 256))


def main():

    part1()
    part2()


if __name__ == "__main__":
    main()
