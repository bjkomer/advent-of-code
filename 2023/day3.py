import numpy as np
from collections import defaultdict

symbols = [
    "@",
    "#",
    "$",
    "%",
    "&",
    "*",
    "-",
    "+",
    "=",
    "/",
]

numbers = [
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
]

def part1(fname="day3_input.txt"):
    with open(fname, 'r') as f:
        lines = f.readlines()
        symbol_array = np.zeros((len(lines), len(lines[0])-1))
        total = 0
        for i, line in enumerate(lines):
            for j, char in enumerate(line[:-1]):
                if char in symbols:
                    symbol_array[i, j] = 1
        for i, line in enumerate(lines):
            current_number = ""
            start_ind = 0
            for j, char in enumerate(line):  # including newline to simplify logic
                if char in numbers:
                    current_number += char
                else:
                    if len(current_number) > 0 and len(np.where(symbol_array[max(0, i-1):i+2, start_ind:j+1] == 1)[0]) > 0:
                        total += int(current_number)
                    start_ind = j
                    current_number = ""
    return total

def part2(fname="day3_input.txt"):
    with open(fname, 'r') as f:
        lines = f.readlines()
        gear_array = np.zeros((len(lines), len(lines[0])-1))
        gears = defaultdict(lambda: list())
        total = 0
        for i, line in enumerate(lines):
            for j, char in enumerate(line[:-1]):
                if char == "*":
                    gear_array[i, j] = 1
        for i, line in enumerate(lines):
            current_number = ""
            start_ind = 0
            for j, char in enumerate(line):  # including newline to simplify logic
                if char in numbers:
                    current_number += char
                else:
                    if len(current_number) > 0:
                        gear_inds = np.where(gear_array[max(0, i-1):i+2, start_ind:j+1] == 1)
                        for x, y in zip(*gear_inds):
                            if i == 0:
                                gears[(x + i, y + start_ind)].append(int(current_number))
                            else:
                                gears[(x + i - 1, y + start_ind)].append(int(current_number))
                    start_ind = j
                    current_number = ""
        for gear, nums in gears.items():
            if len(nums) == 2:
                total += nums[0] * nums[1]
    return total


print(part1("day3_test.txt"))
print(part1("day3_input.txt"))
print(part2("day3_test.txt"))
print(part2("day3_input.txt"))
