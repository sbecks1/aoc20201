from dataclasses import dataclass
from typing_extensions import Self

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


def part1():

    total_fish = 0
    for fish in fishes:
        total_fish += lifetime_reproduction(fish, 80)
    print(total_fish)


def part2():
    total_fish = 0
    for fish in fishes:
        total_fish += lifetime_reproduction(fish, 256)
    print(total_fish)


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
