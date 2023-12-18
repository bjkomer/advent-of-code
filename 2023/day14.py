import numpy as np
from functools import lru_cache

# def roll(slice):
#     rolled = True
#     while rolled:
#         rolled = False
#         for i in range(len(slice)-1):
#             if slice[i] == 0:
#                 if slice[i+1] == 1:
#                     slice[i] = 1
#                     slice[i+1] = 0
#                     rolled = True
#     return slice


@lru_cache(maxsize=1024)
def roll(slice):
    slice = list(slice)
    rolled = True
    while rolled:
        rolled = False
        for i in range(len(slice)-1):
            if slice[i] == 0:
                if slice[i+1] == 1:
                    slice[i] = 1
                    slice[i+1] = 0
                    rolled = True
    return tuple(slice)


@lru_cache(maxsize=1024)
def roll_back(slice):
    slice = list(slice)
    rolled = True
    while rolled:
        rolled = False
        # print(len(slice))
        # print(slice)
        for i in range(len(slice)-1, 0, -1):
            # print(i)
            if slice[i] == 0:
                if slice[i-1] == 1:
                    slice[i] = 1
                    slice[i-1] = 0
                    rolled = True
    return tuple(slice)


@lru_cache(maxsize=1024)
def cycle(rocks):
    rocks = np.array(rocks)
    # North
    for c in range(rocks.shape[1]):
        rocks[:, c] = roll(tuple(rocks[:, c]))
    # West
    for c in range(rocks.shape[0]):
        rocks[c, :] = roll(tuple(rocks[c, :]))
    # South
    for c in range(rocks.shape[1]):
        rocks[:, c] = roll_back(tuple(rocks[:, c]))
    # East
    for c in range(rocks.shape[0]):
        rocks[c, :] = roll_back(tuple(rocks[c, :]))

    return tuple([tuple(r) for r in rocks])


def part1(fname="day14_input.txt"):
    total = 0
    with open(fname, "r") as f:
        lines = f.readlines()
        rocks = np.zeros((len(lines), len(lines[0])-1))
        for i, line in enumerate(lines):
            for j, char in enumerate(line[:-1]):
                if char == "O":
                    rocks[i, j] = 1
                elif char == "#":
                    rocks[i, j] = -1

        for c in range(rocks.shape[1]):
            rocks[:, c] = roll(rocks[:, c])

        for i in range(rocks.shape[0]):
            for j in range(rocks.shape[1]):
                if rocks[i, j] == 1:
                    total += (rocks.shape[0] - i)

    return total


def count(rocks):
    total = 0
    for i in range(len(rocks)):
        for j in range(len(rocks[1])):
            if rocks[i][j] == 1:
                total += (len(rocks) - i)
    return total


def part2(fname="day14_input.txt"):
    total = 0
    with open(fname, "r") as f:
        lines = f.readlines()
        rocks = np.zeros((len(lines), len(lines[0])-1))
        for i, line in enumerate(lines):
            for j, char in enumerate(line[:-1]):
                if char == "O":
                    rocks[i, j] = 1
                elif char == "#":
                    rocks[i, j] = -1

        rocks = tuple([tuple(r) for r in rocks])
        tracking = {}
        max_cycles = 1000000000
        n = 0
        while n < max_cycles:
            rocks = cycle(rocks)
            if rocks in tracking:
                diff = n - tracking[rocks]
                left = 1000000000 - n
                n = max_cycles - (left % diff)
            else:
                tracking[rocks] = n
            print(count(rocks))
            n += 1

        for i in range(len(rocks)):
            for j in range(len(rocks[1])):
                if rocks[i][j] == 1:
                    total += (len(rocks) - i)

    return total


print(part1(fname="day14_test.txt"))
print(part1(fname="day14_input.txt"))
print(part2(fname="day14_test.txt"))
print(part2(fname="day14_input.txt"))
