
num_bounds = []
gears = []

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
            if "*" == input_lines[i][j]:
                gears.append([i, j])

total = 0

for gear in gears:
    nums_near = []
    for num in num_bounds:
        for pos in num["positions"]:
            if abs(pos[0] - gear[0]) < 2 and abs(pos[1] - gear[1]) < 2:
                nums_near.append(int(num["number"]))
                break
    if len(nums_near) == 2:
        total += nums_near[0] * nums_near[1]

print(total)
