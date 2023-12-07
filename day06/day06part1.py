import re

with open("input.txt") as input_text:
	times = re.split(" +", input_text.readline().replace("\n", ""))[1:]
	times = [int(i) for i in times]
	records = re.split(" +", input_text.readline().replace("\n", ""))[1:]
	records = [int(i) for i in records]

total = 1
for i in range(len(times)):
	ways_to_beat = 0
	for j in range(times[i]):
		if j * (times[i] - j) > records[i]:
			ways_to_beat += 1
	total *= ways_to_beat

print(total)
