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
        self.marked_nums = []
        self.remaining_sum = self._calculate_sum()

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
            self._check_bingo(number)

    def _check_bingo(self, called_num: str):
        cols = [list(tup) for tup in list(zip(*self.marks)) if None not in tup]
        if len([row for row in self.marks if None not in row]) > 0 or len(cols) > 0:
            raise BingoCalledException(
                f"""BINGO!!!! 
                    Marked:
                    {self.marks[0]}
                    {self.marks[1]}
                    {self.marks[2]}
                    {self.marks[3]}
                    {self.marks[4]}
                    Num called: {called_num}
                    Remaining: {self.remaining_sum}
                    Score: {int(called_num)*self.remaining_sum}"""
            )


def part1():
    raw_cards = parse_card_data(data)
    bingo_cards = [BingoCard(card) for card in raw_cards]
    for num in called_nums:
        try:
            for card in bingo_cards:
                card.mark_number(num)
        except BingoCalledException as bingo:
            print(bingo)
            break


def main():
    part1()


if __name__ == "__main__":
    main()
