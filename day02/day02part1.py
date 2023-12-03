
MAX_CUBES = {"red": 12,"green": 13, "blue": 14}

sum_possible_ids = 0

with open("input.txt") as inputText:
    lines = inputText.readlines()
    for i in range(len(lines)):
        sets = lines[i].replace("\n", "").split(":")[1]
        game_possible = True
        for cube_set in sets.split(";"):
            for cube in cube_set.split(","):
                cube_num_color = cube.split(" ")
                if int(cube_num_color[1]) > MAX_CUBES[cube_num_color[2]]:
                    game_possible = False
        if game_possible:
            sum_possible_ids += i + 1

print(sum_possible_ids)
