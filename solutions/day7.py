from collections import Counter
import math

with open("inputs/day7.txt") as f:
    data = f.read().rstrip().split(",")


def part1(data) -> int:
    min_fuel = math.inf
    position_counts = Counter(data)
    for org in position_counts:
        fuel_use = 0
        for dest, val in position_counts.items():
            fuel_use += abs(int(org) - int(dest)) * int(val)
        if fuel_use < min_fuel:
            min_fuel = fuel_use
    return min_fuel


print(part1(data))
