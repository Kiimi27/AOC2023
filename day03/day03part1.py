
import re

num_bounds = []
symbols = []

with open("input.txt") as input_text:
    input_lines = input_text.readlines()

for i in range(len(input_lines)):
    cur_num = ""
    num_pos = []
    for j in range(len(input_lines[i])):
        if input_lines[i][j].isdigit():
            num_pos.append([i, j])
            cur_num += input_lines[i][j]
        else:
            if not cur_num == "":
                num_bounds.append({"number": cur_num, "positions": num_pos})
                cur_num = ""
                num_pos = []
            if re.match("[^a-z0-9.\n]", input_lines[i][j]):
                symbols.append([i, j])

total = 0

for num in num_bounds:
    symbol_near = False
    for pos in num["positions"]:
        for symbol in symbols:
            if abs(pos[0] - symbol[0]) < 2 and abs(pos[1] - symbol[1]) < 2:
                symbol_near = True
                break
        if symbol_near:
            total += int(num["number"])
            break

print(total)
