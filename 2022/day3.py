def score_func(char):
	if char.islower():
		return ord(char) - 96
	elif char.isupper():
		return ord(char) - 64 + 26
	else:
		raise ValueError

def part1():
	score = 0
	with open("day3_input.txt", "r") as f:
		for line in f.readlines():
			clean_line = line.strip()
			first_half = {}
			for i, char in enumerate(clean_line):
				if i < len(clean_line) // 2:
					first_half[char] = True
				else:
					if char in first_half.keys():
						score += score_func(char)
						break
	return score

def char_extract(line):
	char_dict = {}
	for char in line:
		char_dict[char] = True
	return char_dict

def part2():
	score = 0
	groupings = []

	with open("day3_input.txt", "r") as f:
		for i, line in enumerate(f.readlines()):
			if i % 3 == 0:
				# Create a new group
				groupings = []
			clean_line = line.strip()
			if i % 3 == 2:
				# Calculate score for the group
				for char in clean_line:
					if char in groupings[0].keys() and char in groupings[1].keys():
						score += score_func(char)
						break
			else:
				# Save information to calculate the score later
				groupings.append(char_extract(clean_line))
	return score


print(part1())
print(part2())
