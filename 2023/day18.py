import numpy as np
import scipy

dir_map = {
    "U": (-1, 0),
    "D": (1, 0),
    "R": (0, 1),
    "L": (0, -1)
}


def part1(fname="day18_input.txt"):
    with open(fname, "r") as f:
        lines = f.readlines()
        loc = (0, 0)
        dug = {(0, 0): 1}
        min_x = 0
        min_y = 0
        max_x = 0
        max_y = 0
        for line in lines:
            d, n, c = line[:-1].split(" ")
            n = int(n)

            for i in range(n):
                offset = dir_map[d]
                loc = (loc[0]+offset[0], loc[1]+offset[1])
                dug[loc] = 1
                min_x = min(min_x, loc[0])
                max_x = max(max_x, loc[0])
                min_y = min(min_y, loc[1])
                max_y = max(max_y, loc[1])
        arr = np.ones((max_x - min_x+1, max_y - min_y+1))
        print(min_x, min_y, max_x, max_y)
        for key, value in dug.items():
            arr[key[0]-min_x, key[1]-min_y] = 0

        labels, n_labels = scipy.ndimage.label(arr)

        # clear out edges
        for i in range(arr.shape[0]):
            if labels[i, 0] != 0:
                labels[np.where(labels==labels[i, 0])] = -1
            if labels[i, -1] != 0:
                labels[np.where(labels==labels[i, -1])] = -1
        for i in range(arr.shape[1]):
            if labels[0, i] != 0:
                labels[np.where(labels==labels[0, 1])] = -1
            if labels[-1, i] != 0:
                labels[np.where(labels==labels[-1, i])] = -1

        return len(np.where(labels>=0)[0])


dir_hex_map = {
    "3": (-1, 0),
    "1": (1, 0),
    "0": (0, 1),
    "2": (0, -1)
}


def decode(hex):
    distance = hex[2:-2]
    direction = hex[-2]

    return direction, int(distance, 16)


def part2(fname="day18_input.txt"):
    with open(fname, "r") as f:
        lines = f.readlines()
        loc = (0, 0)
        dug = {(0, 0): 1}
        min_x = 0
        min_y = 0
        max_x = 0
        max_y = 0
        for line in lines:
            d, n = decode(line[:-1].split(" ")[2])
            n = int(n)

            for i in range(n):
                offset = dir_hex_map[d]
                loc = (loc[0]+offset[0], loc[1]+offset[1])
                dug[loc] = 1
                min_x = min(min_x, loc[0])
                max_x = max(max_x, loc[0])
                min_y = min(min_y, loc[1])
                max_y = max(max_y, loc[1])

        # clear space from the edges
        total = (max_x - min_x + 1) * (max_y - min_y + 1)

        edges = {}
        to_check = []

        for i in range(min_x, max_x + 1):
            if (i, min_y) not in dug:
                to_check.append((i, min_y))
                edges[(i, min_y)] = 1
            if (i, max_y) not in dug:
                to_check.append((i, max_y))
                edges[(i, max_y)] = 1

        for i in range(min_y, max_y + 1):
            if (min_x, i) not in dug:
                to_check.append((min_x, i))
                edges[(min_x, i)] = 1
            if (max_x, i) not in dug:
                to_check.append((max_x, i))
                edges[(max_x, i)] = 1

        while len(to_check) > 0:
            cur_check = to_check.pop()
            # edges[cur_check] = 1
            for offset in dir_hex_map.values():
                next_check = (cur_check[0] + offset[0], cur_check[1] + offset[1])
                if next_check not in edges and next_check not in dug:
                    if min_x <= next_check[0] <= max_x and min_y <= next_check[1] <= max_y:
                        edges[next_check] = 1
                        to_check.append(next_check)

        total -= len(edges.keys())

        return total


print(part1(fname="day18_test.txt"))
print(part1(fname="day18_input.txt"))
print(part2(fname="day18_test.txt"))
print(part2(fname="day18_input.txt"))
