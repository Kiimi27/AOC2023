
maps = []

with open("input.txt") as input_text:
	seeds = input_text.readline().split(" ")[1:]
	seeds = [int(i) for i in seeds]

	map_groups = input_text.read().split("\n\n")

	for i in range(len(map_groups)):
		map_lines = map_groups[i].split("\n")
		maps.append({})

		for j in range(1, len(map_lines)):
			nums = map_lines[j].split(" ")
			maps[i] = {"dest": int(nums[0]), "start": int(nums[1]), "range": int(nums[2])}

	for map_thingy in maps:
		for




