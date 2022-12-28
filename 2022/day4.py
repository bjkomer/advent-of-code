def part1():
	count = 0
	with open("day4_input.txt", "r") as f:
		for line in f.readlines():
			first, second = line.strip().split(',')
			first_start, first_end = first.split('-')
			second_start, second_end = second.split('-')

			if int(first_start) <= int(second_start) and int(first_end) >= int(second_end):
				count += 1
			elif int(second_start) <= int(first_start) and int(second_end) >= int(first_end):
				count += 1
	return count

def part2():
	count = 0
	with open("day4_input.txt", "r") as f:
		for line in f.readlines():
			first, second = line.strip().split(',')
			first_start, first_end = first.split('-')
			second_start, second_end = second.split('-')

			# Easiest to check if no overlap, and count up otherwise
			if not (int(first_end) < int(second_start) or int(second_end) < int(first_start)):
				count += 1
	return count


print(part1())
print(part2())
