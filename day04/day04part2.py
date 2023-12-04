
import re

cards = []

with open("input.txt") as input_text:
    for line in input_text.readlines():
        winning_numbers = re.split(" +", line.split(" | ")[0].split(": ")[1])
        own_numbers = re.split(" +", line.replace("\n", "").split(" | ")[1])
        card_num = int(line.split(":")[0].split(" ")[-1])
        cards.append({"num": card_num, "winning": winning_numbers, "own": own_numbers, "copies": 1})

total = 0

for i in range(len(cards)):
    card = cards[i]
    card_wins = 0
    for win_num in card["winning"]:
        for own_num in card["own"]:
            if win_num == own_num:
                card_wins += 1
                break
    for j in range(1, card_wins + 1):
        if i + j < len(cards):
            cards[i + j]["copies"] += card["copies"]
    total += card["copies"]

print(total)
