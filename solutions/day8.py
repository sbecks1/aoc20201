with open("inputs/day8.txt") as f:
    lines = f.readlines()
    output_vals = [line.split("|")[1].strip() for line in lines]
    signal_patterns = [line.split("|")[0].strip() for line in lines]


def signal_decoder(pattern) -> dict[str, str]:
    decoded = {}
    segments = {}
    known = {7: "8", 3: "7", 4: "4", 2: "1"}
    for digit in pattern.split(" "):
        if len(segments) == 4:
            break
        if len(digit) in known:
            decoded["".join(sorted(digit))] = known[len(digit)]
            segments[known[len(digit)]] = digit

    for digit in pattern.split(" "):

        if len(digit) == 6:  # 0,6,9
            if len(set(segments["1"]) - set(digit)) == 1:
                decoded["".join(sorted(digit))] = "6"
                segments["6"] = digit
            elif len(set(segments["4"]) - set(digit)) == 0:
                decoded["".join(sorted(digit))] = "9"
                segments["9"] = digit
            else:
                decoded["".join(sorted(digit))] = "0"
                segments["0"] = digit

        elif len(digit) == 5:  # 2,3,5
            if len(set(segments["4"]) - set(digit)) == 2:
                decoded["".join(sorted(digit))] = "2"
                segments["2"] = digit
            elif len(set(segments["1"]) - set(digit)) == 0:
                decoded["".join(sorted(digit))] = "3"
                segments["3"] = digit
            else:
                decoded["".join(sorted(digit))] = "5"
                segments["5"] = digit

    return decoded


def part1(vals) -> int:
    lengths_1478 = [2, 4, 3, 7]

    known_digits = 0

    for line in vals:
        for digit in line.split(" "):
            if len(digit) in lengths_1478:
                known_digits += 1

    return known_digits


def part2(signals, outputs) -> int:

    sum_output = 0

    for signal, out in zip(signals, outputs):
        decoded_output = ""
        decoder = signal_decoder(signal)
        for digit in out.split(" "):
            decoded_output += decoder["".join(sorted(digit))]
        sum_output += int(decoded_output)

    return sum_output


def main():
    print(part1(output_vals))
    print(part2(signal_patterns, output_vals))


if __name__ == "__main__":
    main()
