import math

hands = {"fives": [], "fours": [], "fulls": [], "threes": [], "twopairs": [], "onepairs": [], "rest": []}
labels = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]


def get_hand_worth(hand):
	worth = [0, 0, 0, 0, 0]
	for i in range(len(hand["cards"])):
		worth[i] = labels.index(hand["cards"][i])
	return worth


with open("input.txt") as input_text:
	for line in input_text.readlines():
		hand_line = line.split(" ")
		cards = hand_line[0]
		bid = hand_line[1].replace("\n", "")
		hand = {"cards": cards, "bid": bid}

		label_counts = [0 for i in range(len(labels) - 1)]
		joker_count = cards.count("J")

		for i in range(len(labels) - 1):
			label_counts[i] = cards.count(labels[i])

		label_counts.sort(reverse=True)

		if label_counts[0] == 5:
			hands["fives"].append(hand)
		elif label_counts[0] == 4:
			if joker_count == 1:
				hands["fives"].append(hand)
			else:
				hands["fours"].append(hand)
		elif label_counts[0] == 3:
			if joker_count == 2:
				hands["fives"].append(hand)
			elif joker_count == 1:
				hands["fours"].append(hand)
			elif label_counts[1] == 2:
				hands["fulls"].append(hand)
			else:
				hands["threes"].append(hand)
		elif label_counts[0] == 2:
			if joker_count == 3:
				hands["fives"].append(hand)
			elif joker_count == 2:
				hands["fours"].append(hand)
			elif joker_count == 1:
				if label_counts[1] == 2:
					hands["fulls"].append(hand)
				else:
					hands["threes"].append(hand)
			elif label_counts[1] == 2:
				hands["twopairs"].append(hand)
			else:
				hands["onepairs"].append(hand)
		else:
			if joker_count == 5 or joker_count == 4:
				hands["fives"].append(hand)
			elif joker_count == 3:
				hands["fours"].append(hand)
			elif joker_count == 2:
				hands["threes"].append(hand)
			elif joker_count == 1:
				hands["onepairs"].append(hand)
			else:
				hands["rest"].append(hand)


for hand_type in hands:
	print(hand_type)
	hands_sorted = False
	hands[hand_type].sort(key=get_hand_worth)
	for hand in hands[hand_type]:
		print(hand["cards"])

all_hands = hands["fives"]
all_hands.extend(hands["fours"])
all_hands.extend(hands["fulls"])
all_hands.extend(hands["threes"])
all_hands.extend(hands["twopairs"])
all_hands.extend(hands["onepairs"])
all_hands.extend(hands["rest"])

winnings = 0

for i in reversed(range(len(all_hands))):
	winnings += int(all_hands[i]["bid"]) * (len(all_hands) - i)

print(winnings)

