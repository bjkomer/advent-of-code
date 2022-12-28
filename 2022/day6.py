def all_unique(data):
	check = {}
	for char in data:
		check[char] = True
	return len(check.keys()) == len(data)

def part1(fname="day6_input.txt"):
	with open(fname, "r") as f:
		line = f.readlines()[0]

	for i in range(3, len(line)):
		if all_unique(line[i-3:i+1]):
			return i + 1


def part2(fname="day6_input.txt"):
	with open(fname, "r") as f:
		line = f.readlines()[0]

	for i in range(13, len(line)):
		if all_unique(line[i-13:i+1]):
			return i + 1


print(part1())
print(part2())
