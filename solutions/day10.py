with open("inputs/day10.txt") as f:
    data = [line.strip() for line in f.readlines()]

test_data = [
    "[({(<(())[]>[[{[]{<()<>>",
    "[(()[<>])]({[<{<<[]>>(",
    "{([(<{}[<>[]}>{[]{[(<()>",
    "(((({<>}<{<{<>}{[]{[]{}",
    "[[<[([]))<([[{}[[()]]]",
    "[{[{({}]{}}([{[{{{}}([]",
    "{<[[]]>}<{[{[{[]{()[[[]",
    "[<(<(<(<{}))><([]([]()",
    "<{([([[(<>()){}]>(<<{{",
    "<{([{{}}[<[[[<>{}]]]>[]]",
]


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


def is_incomplete(line: str) -> bool:
    pass


def calc_error_score(line: str) -> int:
    scores = {")": 3, "]": 57, "}": 1197, ">": 25137}

    first_illegal = min([line.index(key) for key in scores if key in line])
    return scores[line[first_illegal]]


def part1():
    cumulative_error = 0
    for line in data:
        if is_corrupt(line):
            cumulative_error += calc_error_score(remove_empty_chunks(line))
    print(cumulative_error)


def main():
    part1()


if __name__ == "__main__":
    main()
