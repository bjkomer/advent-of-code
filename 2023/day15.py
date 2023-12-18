import numpy as np
from functools import lru_cache
from collections import defaultdict


def part1(fname="day15_input.txt"):
    totals = 0
    with open(fname, "r") as f:
        line = f.readline()[:-1]
        steps = line.split(",")
        for step in steps:
            total = 0
            for char in step:
                total += ord(char)
                total *= 17
                total = total % 256
            totals += total
    return totals


def h(step):
    total = 0
    for char in step:
        total += ord(char)
        total *= 17
        total = total % 256
    return total


def part2(fname="day15_input.txt"):
    total = 0
    boxes = defaultdict(lambda: [])
    with open(fname, "r") as f:
        line = f.readline()[:-1]
        steps = line.split(",")
        for step in steps:
            if "=" in step:
                s, lens = step.split("=")
                lens = int(lens)
                box = h(s)
                for i in range(len(boxes[box])):
                    if boxes[box][i][0] == s:
                        boxes[box][i] = (s, lens)
                        break
                else:
                    boxes[box].append((s, lens))
            elif "-" in step:
                s = step[:-1]
                box = h(s)
                for i in range(len(boxes[box])):
                    if boxes[box][i][0] == s:
                        del boxes[box][i]
                        break

    for i in range(255):
        for j, pair in enumerate(boxes[i]):
            total += (i+1)*(j+1)*pair[1]
    return total


print(part1(fname="day15_test.txt"))
print(part1(fname="day15_input.txt"))
print(part2(fname="day15_test.txt"))
print(part2(fname="day15_input.txt"))
