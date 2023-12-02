
sum_fewest_possible_power = 0

with open("input.txt") as inputText:
    lines = inputText.readlines()
    for i in range(len(lines)):
        sets = lines[i].replace("\n", "").split(":")[1]
        fewest_cubes = {"red": 0, "green": 0, "blue": 0}
        for cube_set in sets.split(";"):
            for cube in cube_set.split(","):
                cube_num_color = cube.split(" ")
                if int(cube_num_color[1]) > fewest_cubes[cube_num_color[2]]:
                    fewest_cubes[cube_num_color[2]] = int(cube_num_color[1])
        sum_fewest_possible_power += fewest_cubes["red"] * fewest_cubes["green"] * fewest_cubes["blue"]

print(sum_fewest_possible_power)
