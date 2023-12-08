import re

nodes = {}

with open("input.txt") as input_text:
	directions_line = input_text.readline().replace("\n", "")
	input_text.readline()

	for line in input_text.readlines():
		line_nodes = re.findall("[A-Z]{3}", line)
		nodes[line_nodes[0]] = {"L": line_nodes[1], "R": line_nodes[2]}

current_pos = "AAA"
steps = 0

while not current_pos == "ZZZ":
	current_pos = nodes[current_pos][directions_line[steps % len(directions_line)]]
	steps += 1

print(steps)
