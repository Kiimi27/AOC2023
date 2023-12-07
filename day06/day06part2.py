import re

with open("input.txt") as input_text:
	time = ""
	time_nums = re.split(" +", input_text.readline().replace("\n", ""))[1:]
	for time_num in time_nums:
		time += time_num
	record = ""
	record_nums = re.split(" +", input_text.readline().replace("\n", ""))[1:]
	for record_num in record_nums:
		record += record_num


ways_to_beat = 0
for j in range(int(time)):
	if j * (int(time) - j) > int(record):
		ways_to_beat += 1

print(ways_to_beat)
