with open("inputs/day10.txt") as f:
    data = [line.strip() for line in f.readlines()]


def remove_empty_chunks(line: str) -> str:
    string = line
    empties = ["()", "<>", "{}", "[]"]
    all_empties_removed = False
    while not all_empties_removed:
        for empty in empties:
            string = string.replace(empty, "")
        all_empties_removed = all([empty not in string for empty in empties])

    return string


def is_corrupt(line: str) -> bool:
    closers = [")", "]", ">", "}"]
    return any(closer in remove_empty_chunks(line) for closer in closers)


def calc_error_score(line: str) -> int:
    scores = {")": 3, "]": 57, "}": 1197, ">": 25137}

    first_illegal = min([line.index(key) for key in scores if key in line])
    return scores[line[first_illegal]]


def get_closing_chars(fragment: str) -> str:
    open_to_close = {"(": ")", "{": "}", "[": "]", "<": ">"}

    return "".join([open_to_close[char] for char in reversed(fragment)])


def get_autocomplete_score(closing: str) -> int:
    points = {")": 1, "]": 2, "}": 3, ">": 4}

    score = 0
    for char in closing:
        score = (score * 5) + points[char]
    return score


def part1():
    cumulative_error = 0
    for line in data:
        if is_corrupt(line):
            cumulative_error += calc_error_score(remove_empty_chunks(line))
    print(cumulative_error)


def part2():
    scores = []
    for line in data:
        if not is_corrupt(line):
            score = get_autocomplete_score(get_closing_chars(remove_empty_chunks(line)))
            scores.append(score)

    ranked = sorted(scores)
    print(ranked[len(ranked) // 2])


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
