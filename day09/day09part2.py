total = 0

with open("input.txt") as input_text:
	for line in input_text.readlines():
		sequences = [[int(i) for i in line.replace("\n", "").replace("\x00", "").split(" ")]]
		i = 0
		while any([k != 0 for k in sequences[i]]):
			next_sequence = []
			for j in range(1, len(sequences[i])):
				next_sequence.append(sequences[i][j] - sequences[i][j - 1])
			sequences.append(next_sequence)
			i += 1
		extrapolated_num = 0
		for sequence in reversed(sequences[:-1]):
			extrapolated_num = sequence[0] - extrapolated_num
		print(extrapolated_num)
		total += extrapolated_num

print(total)
