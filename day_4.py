def get_input():
    with open("day-4.txt", "r") as input:
        bingo_numbers = input.readline()

        cards_string = input.readlines()
        cards = []
        for line in cards_string:
            cards.append(list(map(int, line.split())))
        cards = [row for row in cards if len(row) > 0]

        return (list(map(int, bingo_numbers.split(","))), cards)

def check_off_number(bingo_number, cards):
    new_cards = []
    for row in cards:
        new_row = []
        for digit in row:
            new_row.append(None if digit == bingo_number else digit)
        new_cards.append(new_row)

    return new_cards

def select_card(card_index, cards):
    row_number = card_index * 5
    return cards[row_number:row_number + 5]

def is_card_bingo(card):
    # check rows
    for row in card:
        if all(digit is None for digit in row):
            return True

    # check cols
    for col in range (0,5):
        column = [row[col] for row in card]
        if all(digit is None for digit in column):
            return True

    return False

def check_for_bingo(cards):
    cards_done = []

    for i in range(0, 100):
        card = select_card(i, cards)
        cards_done.append(i if is_card_bingo(card) else None)
    return cards_done


## main

(bingo_numbers, cards) = get_input()
bingo_card_indexes = [None]
card_indexes = range(0, int(len(cards)/5))
last_card = None

while bingo_numbers and None in bingo_card_indexes:

    last_card = [i for i, val in enumerate(bingo_card_indexes) if val == None]

    current_bingo_number = bingo_numbers.pop(0)
    cards = check_off_number(current_bingo_number, cards)
    bingo_card_indexes = check_for_bingo(cards)

card = select_card(last_card[0], cards)
card_sum = sum([digit for row in card for digit in row if digit is not None])
print(card_sum * current_bingo_number)