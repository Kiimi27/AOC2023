import sys
import math

sys.setrecursionlimit(100000)


def check_loop(cur_pos, con, stp):
	if con[0] == starting_pipe["x"] and con[1] == starting_pipe["y"]:
		return stp
	if con in pipes:
		for next_connection in pipes[con]["cons"]:
			if not next_connection == cur_pos:
				return check_loop(pipes[con]["pos"], (next_connection["x"], next_connection["y"]), stp + 1)
	else:
		return -1
	return stp


pipe_types = {"|": [{"x": 0, "y": 1}, {"x": 0, "y": -1}], "-": [{"x": 1, "y": 0}, {"x": -1, "y": 0}], "L": [{"x": 1, "y": 0}, {"x": 0, "y": -1}], "J": [{"x": -1, "y": 0}, {"x": 0, "y": -1}], "7": [{"x": -1, "y": 0}, {"x": 0, "y": 1}], "F": [{"x": 1, "y": 0}, {"x": 0, "y": 1}]}
pipes = {}

with open("input.txt") as input_text:
	lines = input_text.readlines()
	for y in range(len(lines)):
		for x in range(len(lines[y])):
			if lines[y][x] in pipe_types:
				pipes[(x, y)] = {"pos": {"x": x, "y": y}, "cons": [{"x": x + pipe_types[lines[y][x]][0]["x"], "y": y + pipe_types[lines[y][x]][0]["y"]}, {"x": x + pipe_types[lines[y][x]][1]["x"], "y": y + pipe_types[lines[y][x]][1]["y"]}]}
			elif lines[y][x] == "S":
				starting_pipe = {"x": x, "y": y}

	back_at_start = False
	while not back_at_start:
		for connection in [(starting_pipe["x"] + 1, starting_pipe["y"]), (starting_pipe["x"] - 1, starting_pipe["y"]), (starting_pipe["x"], starting_pipe["y"] + 1), (starting_pipe["x"], starting_pipe["y"] - 1)]:
			steps = check_loop(starting_pipe, connection, 0)
			if steps > 0:
				back_at_start = True
				break

	print(math.ceil(steps / 2))
