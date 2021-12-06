from dataclasses import dataclass
from typing_extensions import Self

with open("inputs/day6.txt") as f:
    ages = f.read().rstrip().split(",")

fish: list[int] = [int(age) for age in ages]


def model_latern_fish(fish: list[int], num_steps: int) -> list[int]:
    new_fish = []
    for i in range(num_steps):
        for i, lf in enumerate(fish):

            if lf == 0:
                fish[i] = 6
                new_fish.append(0)
                continue

            fish[i] -= 1
        fish.extend(new_fish.copy())
        new_fish = []

    return fish


def part1():
    num_fish = len(model_latern_fish(fish, 40))
    print(num_fish)


def main():
    part1()


if __name__ == "__main__":
    main()
