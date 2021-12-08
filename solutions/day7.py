import math

with open("inputs/day7.txt") as f:
    data = [int(n) for n in f.read().rstrip().split(",")]


def part1(data) -> int:
    min_fuel = math.inf
    for org in data:
        fuel_use = 0
        for dest in data:
            fuel_use += abs(org - dest)
        if fuel_use < min_fuel:
            min_fuel = fuel_use
    return min_fuel


def part2(data) -> int:
    min_fuel = math.inf
    for org in range(min(data), max(data) + 1):  # forget unoccupied positions
        fuel_use = 0

        for dest in data:
            fuel_use += sum(range(abs(int(dest) - int(org)) + 1))

        if fuel_use < min_fuel:
            min_fuel = fuel_use

    return min_fuel


print(part1(data))
print(part2(data))
