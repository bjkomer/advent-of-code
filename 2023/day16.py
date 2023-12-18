import numpy as np
from functools import lru_cache
from collections import defaultdict


dir_map = {
    "R": 0,
    "L": 1,
    "D": 2,
    "U": 3,
}

offset_to_index = {
    (0, 1): 0,
    (0, -1): 1,
    (1, 0): 2,
    (-1, 0): 3
}

directions = {
    ".": {
        0: [(0, 1)],
        1: [(0, -1)],
        2: [(1, 0)],
        3: [(-1, 0)],
    },
    "|": {
        0: [(1, 0), (-1, 0)],
        1: [(1, 0), (-1, 0)],
        2: [(1, 0)],
        3: [(-1, 0)],
    },
    "-": {
        0: [(0, 1)],
        1: [(0, -1)],
        2: [(0, 1), (0, -1)],
        3: [(0, 1), (0, -1)],
    },
    "/": {
        0: [(-1, 0)],
        1: [(1, 0)],
        2: [(0, -1)],
        3: [(0, 1)],
    },
    "\\": {
        0: [(1, 0)],
        1: [(-1, 0)],
        2: [(0, 1)],
        3: [(0, -1)],
    },
}


def part1(fname="day15_input.txt"):
    total = 0
    with open(fname, "r") as f:
        lines = f.readlines()
        height = len(lines)
        width = len(lines[0]) - 1
        arr = np.zeros((height, width, 4))
        beams_left = [(0, 0, 0)]
        while len(beams_left) > 0:
            cb = beams_left.pop()
            if 0 <=cb[0] < height and 0 <= cb[1] < width and arr[cb[0], cb[1], cb[2]] == 0:
                arr[cb[0], cb[1], cb[2]] = 1
                nbs = directions[lines[cb[0]][cb[1]]][cb[2]]
                for nb in nbs:
                    beams_left.append((cb[0]+nb[0], cb[1]+nb[1], offset_to_index[nb]))

        for i in range(height):
            for j in range(width):
                if np.sum(arr[i, j, :]) > 0:
                    total += 1

    return total


def part2(fname="day16_input.txt"):
    with open(fname, "r") as f:
        lines = f.readlines()
        height = len(lines)
        width = len(lines[0]) - 1
        best = 0

        starts = []

        for i in range(height):
            starts.append((i, 0, 0))
            starts.append((i, width-1, 1))

        for i in range(width):
            starts.append((0, i, 2))
            starts.append((height - 1, i, 3))

        for start in starts:
            total = 0
            arr = np.zeros((height, width, 4))
            beams_left = [start]
            while len(beams_left) > 0:
                cb = beams_left.pop()
                if 0 <=cb[0] < height and 0 <= cb[1] < width and arr[cb[0], cb[1], cb[2]] == 0:
                    arr[cb[0], cb[1], cb[2]] = 1
                    nbs = directions[lines[cb[0]][cb[1]]][cb[2]]
                    for nb in nbs:
                        beams_left.append((cb[0]+nb[0], cb[1]+nb[1], offset_to_index[nb]))

            for i in range(height):
                for j in range(width):
                    if np.sum(arr[i, j, :]) > 0:
                        total += 1
            best = max(best, total)

    return best


print(part1(fname="day16_test.txt"))
print(part1(fname="day16_input.txt"))
print(part2(fname="day16_test.txt"))
print(part2(fname="day16_input.txt"))
