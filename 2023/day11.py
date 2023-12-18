import numpy as np


def expand_dist(start, end, expand_list, expansion_amount=2):
    dist = 0

    if start > end:
        start, end = end, start

    for i in range(start, end):
        if i in expand_list:
            dist += expansion_amount
        else:
            dist += 1

    return dist


def part1(fname="day11_input.txt", expansion_amount=2):
    planets = []
    expand_xs = []
    expand_ys = []
    with open(fname, "r") as f:
        lines = f.readlines()
        arr = np.zeros((len(lines), len(lines[0])-1))
        for x, line in enumerate(lines):
            for y, char in enumerate(line[:-1]):
                if char == "#":
                    arr[x, y] = 1
                    planets.append((x, y))
        for x in range(arr.shape[0]):
            if np.sum(arr[x, :]) == 0:
                expand_xs.append(x)
        for y in range(arr.shape[1]):
            if np.sum(arr[:, y]) == 0:
                expand_ys.append(y)
        dists = 0

        for i in range(len(planets)):
            for j in range(i + 1, len(planets)):
                dists += expand_dist(planets[i][0], planets[j][0], expand_xs, expansion_amount)
                dists += expand_dist(planets[i][1], planets[j][1], expand_ys, expansion_amount)

        return dists


def part2(fname="day11_input.txt"):
    return part1(fname, expansion_amount=1000000)


print(part1(fname="day11_test.txt"))
print(part1(fname="day11_input.txt"))
print(part2(fname="day11_test.txt"))
print(part2(fname="day11_input.txt"))
