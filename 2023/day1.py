number_map = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "0": "0",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
}


def get_number(line):
    num_str = ''
    for c in line:
        if c in '0123456789':
            num_str += c
            break
    for c in reversed(line):
        if c in '0123456789':
            num_str += c
            break

    return int(num_str)

def get_spelled_number(line):
    num_str = ''
    for i, line_check in enumerate([line, line[::-1]]):
        best_ind = len(line_check)
        best_num = ''
        for num_check, num in number_map.items():
            if i == 0:
                ind = line_check.find(num_check)
            else:
                ind = line_check.find(num_check[::-1])
            if ind != -1:
                if ind < best_ind:
                    best_ind = ind
                    best_num = num
        assert best_num != ""
        num_str += best_num
    return int(num_str)

def part1(fname="day1_input.txt"):
    total = 0

    with open(fname, "r") as f:
        for line in f.readlines():
            total += get_number(line)

    return total

def part2(fname="day1_input.txt"):
    total = 0

    with open(fname, "r") as f:
        for line in f.readlines():
            total += get_spelled_number(line)

    return total

print(part1())
print(part2())

