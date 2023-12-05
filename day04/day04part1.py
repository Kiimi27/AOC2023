
import re

total = 0

with open("input.txt") as input_text:
    for line in input_text.readlines():
        line_worth = 0
        winning_numbers = re.split(" +", line.split(" | ")[0].split(": ")[1])
        own_numbers = re.split(" +", line.replace("\n", "").split(" | ")[1])
        for win_num in winning_numbers:
            for own_num in own_numbers:
                if win_num == own_num:
                    if line_worth == 0:
                        line_worth = 1
                    else:
                        line_worth *= 2
                    break
        total += line_worth

print(total)
