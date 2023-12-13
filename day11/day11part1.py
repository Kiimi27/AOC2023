galaxies = []
empty_rows = []
empty_columns = []
total_distance = 0

with open("input.txt") as input_text:
	lines = [line.replace("\n", "") for line in input_text.readlines()]
	for y in range(len(lines)):
		for x in range(len(lines[y])):
			if lines[y][x] == "#":
				galaxies.append({"x": x, "y": y})
		if "#" not in lines[y]:
			empty_rows.append(y)

	for x in range(len(lines[0])):
		if not any([line[x] == "#" for line in lines]):
			empty_columns.append(x)

	for i in range(len(galaxies)):
		for other_galaxy in galaxies[i + 1:]:
			additional_spaces = sum([1 if galaxies[i]["x"] > empty_column > other_galaxy["x"] or galaxies[i]["x"] < empty_column < other_galaxy["x"] else 0 for empty_column in empty_columns]) + sum([1 if galaxies[i]["y"] > empty_row > other_galaxy["y"] or galaxies[i]["y"] < empty_row < other_galaxy["y"] else 0 for empty_row in empty_rows])
			total_distance += additional_spaces + abs(galaxies[i]["x"] - other_galaxy["x"]) + abs(galaxies[i]["y"] - other_galaxy["y"])

print(total_distance)
