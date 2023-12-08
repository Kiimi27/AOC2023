import math
import re

nodes = {}
current_positions = []

with open("input.txt") as input_text:
	directions_line = input_text.readline().replace("\n", "")
	input_text.readline()

	for line in input_text.readlines():
		line_nodes = re.findall("[A-Z]{3}", line)
		if line_nodes[0][-1] == "A":
			current_positions.append(line_nodes[0])
		nodes[line_nodes[0]] = {"L": line_nodes[1], "R": line_nodes[2]}

final_steps = 1

for i in range(len(current_positions)):
	steps = 0
	while not current_positions[i][-1] == "Z":
		current_positions[i] = nodes[current_positions[i]][directions_line[steps % len(directions_line)]]
		steps += 1
	total = math.lcm(final_steps, steps)

print(final_steps)
