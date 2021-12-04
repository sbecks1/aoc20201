with open("inputs/day4.txt") as f:
    lines = f.readlines()

called_nums = lines[0].rstrip().split(",")
data = [line.rstrip().split("\n\n") for line in lines[2:]]


def parse_card_data(data):
    raw_cards = []
    card = []
    for row in data:
        if len(row[0]) > 0:
            card.append([num for num in row[0].split(" ") if num != ""])
        else:
            raw_cards.append(card.copy())
            card = []
    return raw_cards


class BingoCalledException(Exception):
    pass


class BingoCard:
    def __init__(self, raw_card: "list[list[str]]"):
        self.card = raw_card
        self.marks = [
            [None for i in range(len(raw_card))] for i in range(len(raw_card))
        ]
        self.marked_nums: list[int] = []
        self.remaining_sum: int = self._calculate_sum()
        self.has_bingo: bool = False

    def _calculate_sum(self):
        card_sum = 0
        for row in self.card:
            card_sum += sum([int(n) for n in row])
        return card_sum

    def mark_number(self, number: str):
        for idx, row in enumerate(self.card):
            if number in row:
                col_idx = row.index(number)
                self.marks[idx][col_idx] = number
                self.marked_nums.append(int(number))
                self.remaining_sum -= int(number)
        if len(self.marked_nums) >= 5:
            self._set_bingo()

    def _set_bingo(self):
        cols = [list(tup) for tup in list(zip(*self.marks)) if None not in tup]
        if len([row for row in self.marks if None not in row]) > 0 or len(cols) > 0:
            self.has_bingo = True

    def check_bingo(self):
        if self.has_bingo:
            raise BingoCalledException(
                f"""BINGO!!!! 
                        Marked:
                        {self.marks[0]}
                        {self.marks[1]}
                        {self.marks[2]}
                        {self.marks[3]}
                        {self.marks[4]}
                        Num called: {self.marked_nums[-1]}
                        Remaining: {self.remaining_sum}
                        Score: {self.marked_nums[-1]*self.remaining_sum}"""
            )


def part1():
    raw_cards = parse_card_data(data)
    bingo_cards: list[BingoCard] = [BingoCard(card) for card in raw_cards]
    for num in called_nums:
        try:
            for card in bingo_cards:
                card.mark_number(num)
                card.check_bingo()

        except BingoCalledException as bingo:
            print(bingo)
            break


def part2():
    raw_cards = parse_card_data(data)
    bingo_cards: list[BingoCard] = [BingoCard(card) for card in raw_cards]
    bingos: list[BingoCard] = []
    for num in called_nums:
        for card in bingo_cards:
            card.mark_number(num)
            if card.has_bingo:
                bingos.append(card)
                bingo_cards = [card for card in bingo_cards if not card.has_bingo]

    print(bingos[-1].marked_nums[-1] * bingos[-1].remaining_sum)


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
