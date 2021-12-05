import numpy as np


# Part 1
depth = 0
pos = 0
with open("day2_input.txt", "r") as f:
    for line in f.readlines():
        command, val = line.split(" ")
        if command == "forward":
            pos += int(val)
        elif command == "down":
            depth += int(val)
        elif command == "up":
            depth -= int(val)
        else:
            raise ValueError

print(depth * pos)

# Part 2
depth = 0
pos = 0
aim = 0
with open("day2_input.txt", "r") as f:
    for line in f.readlines():
        command, val = line.split(" ")
        if command == "forward":
            pos += int(val)
            depth += aim * int(val)
        elif command == "down":
            aim += int(val)
        elif command == "up":
            aim -= int(val)
        else:
            raise ValueError

print(depth * pos)
