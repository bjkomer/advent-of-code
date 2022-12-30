import numpy as np
import heapq


def parse_input(fname="day12_input.txt"):
    with open(fname, "r") as f:
        lines = f.readlines()
        height = len(lines)
        width = len(lines[0].strip())
        elev = np.zeros((height, width), dtype=np.int16)

        for i, line in enumerate(lines):
            for j, char in enumerate(line.strip()):
                if char == "S":
                    start = np.array([i, j], dtype=np.int16)
                    elev[i, j] = 0
                elif char == "E":
                    end = np.array([i, j], dtype=np.int16)
                    elev[i, j] = 25
                else:
                    elev[i, j] = ord(char) - 97
    return start, end, elev

def shortest_path(start, end, elev):
    # Keep track of how many steps to get to each location
    steps = np.ones_like(elev) * np.iinfo(elev.dtype).max

    checks = [
        np.array([1, 0], dtype=np.int16),
        np.array([-1, 0], dtype=np.int16),
        np.array([0, 1], dtype=np.int16),
        np.array([0, -1], dtype=np.int16),
    ]

    steps[start[0], start[1]] = 0

    # Extra priority field is needed to break ties
    tie_break = 0
    to_expand = [(0, tie_break, start)]
    heapq.heapify(to_expand)

    while len(to_expand) > 0:
        cur_cost, _, cur_node = heapq.heappop(to_expand)

        for check in checks:
            next_node = cur_node + check
            if 0 <= next_node[0] < steps.shape[0] and 0 <= next_node[1] < steps.shape[1]:
                if elev[next_node[0], next_node[1]] <= elev[cur_node[0], cur_node[1]] + 1:
                    if steps[next_node[0], next_node[1]] > cur_cost + 1:
                        steps[next_node[0], next_node[1]] = cur_cost + 1
                        tie_break += 1
                        heapq.heappush(to_expand, (cur_cost + 1, tie_break, next_node))

    return steps[end[0], end[1]]

def part1(fname="day12_input.txt"):
    start, end, elev = parse_input(fname=fname)

    return shortest_path(start, end, elev)

def part2(fname="day12_input.txt"):
    start, end, elev = parse_input(fname=fname)

    # Brute force method
    starts = np.where(elev == 0)

    best_shortest = np.iinfo(elev.dtype).max
    for start in zip(*starts):
        cur_shortest = shortest_path(start, end, elev)
        best_shortest = min(best_shortest, cur_shortest)

    return best_shortest


print(part1())
print(part2())
