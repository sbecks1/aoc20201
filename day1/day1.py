with open("inputs/day1.txt") as f:
    lines = f.readlines()
lines = [int(line.rstrip()) for line in lines]

increased: int = 0

for i, n in enumerate(lines):
    try:
        if lines[i + 1] > n:
            increased += 1
    except IndexError:
        print(f"{increased} increases.")
