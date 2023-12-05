
maps = []

with open("input.txt") as input_text:
	important_numbers = input_text.readline().split(" ")[1:]
	important_numbers = [int(i) for i in important_numbers]

	map_groups = input_text.read().split("\n\n")

	for i in range(len(map_groups)):
		map_lines = map_groups[i][1:].split("\n")
		maps.append([])

		for j in range(1, len(map_lines)):
			nums = map_lines[j].split(" ")
			maps[i].append({"dest": int(nums[0]), "start": int(nums[1]), "range": int(nums[2])})

	for map_thingy in maps:
		for i in range(len(important_numbers)):
			for map_range in map_thingy:
				if map_range["start"] <= important_numbers[i] < map_range["start"] + map_range["range"]:
					important_numbers[i] = map_range["dest"] + important_numbers[i] - map_range["start"]
					break

	lowest_number = important_numbers[0]
	for num in important_numbers[1:]:
		if num < lowest_number:
			lowest_number = num

	print(lowest_number)
