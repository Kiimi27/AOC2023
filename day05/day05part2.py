
maps = []

with open("input.txt") as input_text:
    seed_ranges = input_text.readline().split(" ")[1:]
    seed_ranges = [int(i) for i in seed_ranges]
    important_ranges = []
    for i in range(int(len(seed_ranges) / 2)):
        important_ranges.append({"start": seed_ranges[i*2], "end": seed_ranges[i*2] + seed_ranges[i * 2 + 1] - 1})

    map_groups = input_text.read().split("\n\n")

    for i in range(len(map_groups)):
        map_lines = map_groups[i][1:].split("\n")
        maps.append([])

        for j in range(1, len(map_lines)):
            nums = map_lines[j].split(" ")
            maps[i].append({"dest": {"start": int(nums[0]), "end": int(nums[0]) + int(nums[2]) - 1}, "source": {"start": int(nums[1]), "end": int(nums[1]) + int(nums[2]) - 1}})

    for map_thingy in maps:
        for i in range(len(important_ranges)):
            for map_range in map_thingy:
                if map_range["source"]["start"] <= important_ranges[i]["start"] <= important_ranges[i]["end"] <= map_range["source"]["end"]:
                    important_ranges[i] = {"start": important_ranges[i]["start"] - map_range["source"]["start"] + map_range["dest"]["start"], "end": important_ranges[i]["end"] - map_range["source"]["start"] + map_range["dest"]["start"]}
                    break
                elif map_range["source"]["start"] <= important_ranges[i]["start"] <= map_range["source"]["end"] < important_ranges[i]["end"]:
                    important_ranges.append({"start": important_ranges[i]["start"] + map_range["dest"]["start"] - map_range["source"]["start"],"end": map_range["dest"]["end"]})
                    important_ranges[i]["start"] = map_range["source"]["end"]+1
                elif important_ranges[i]["start"] < map_range["source"]["start"] <= important_ranges[i]["end"] <= map_range["source"]["end"]:
                    important_ranges.append({"start": map_range["dest"]["start"], "end": important_ranges[i]["end"] + map_range["dest"]["start"] - map_range["source"]["start"]})
                    important_ranges[i]["end"] = map_range["source"]["start"]-1

lowest_number = important_ranges[0]["start"]
for num_range in important_ranges[1:]:
    if num_range["start"] < lowest_number:
        lowest_number = num_range["start"]

print(lowest_number)
