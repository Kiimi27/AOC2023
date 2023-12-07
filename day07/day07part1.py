import math

hands = {"fives": [], "fours": [], "fulls": [], "threes": [], "twopairs": [], "onepairs": [], "rest": []}
labels = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]


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

		three = False
		pair = False

		for label in labels:
			label_count = cards.count(label)
			if label_count == 5:
				hands["fives"].append(hand)
				break
			elif label_count == 4:
				hands["fours"].append(hand)
				break
			elif label_count == 3:
				if pair:
					hands["fulls"].append(hand)
					break
				three = True
			elif label_count == 2:
				if three:
					hands["fulls"].append(hand)
					break
				elif pair:
					hands["twopairs"].append(hand)
					break
				pair = True
		else:
			if three:
				hands["threes"].append(hand)
			elif pair:
				hands["onepairs"].append(hand)
			else:
				hands["rest"].append(hand)

for hand_type in hands:
	hands_sorted = False
	hands[hand_type].sort(key=get_hand_worth)

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
