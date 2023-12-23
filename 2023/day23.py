import numpy as np
from functools import lru_cache
import scipy

offsets = (
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
)


def block(line, index):
    return line[:index] + "#" + line[index + 1:]


@lru_cache()
def path_to_end(start, end, cur_map):
    # if cur_map[start[0]][start[1]] == "#":
    #     return -np.inf
    if start == end:
        return 0
    next_vals = []
    for offset in offsets:
        next_node = (start[0] + offset[0], start[1] + offset[1])
        if 0 <= next_node[0] < len(cur_map) and 0 <= next_node[1] < len(cur_map[0]):
            # print(next_node)
            if cur_map[next_node[0]][next_node[1]] == "#":
                continue
            elif cur_map[next_node[0]][next_node[1]] == ">" and offset != (0, 1):
                continue
            elif cur_map[next_node[0]][next_node[1]] == "<" and offset != (0, -1):
                continue
            elif cur_map[next_node[0]][next_node[1]] == "v" and offset != (1, 0):
                continue
            elif cur_map[next_node[0]][next_node[1]] == "^" and offset != (-1, 0):
                continue
            next_map = []
            for i, line in enumerate(cur_map):
                if i == next_node[0]:
                    next_map.append(block(line, next_node[1]))
                else:
                    next_map.append(line)
            next_map = tuple(next_map)
            val = 1 + path_to_end(
                next_node,
                end,
                next_map,
            )
            if val > -1:
                next_vals.append(
                    1 + path_to_end(
                        next_node,
                        end,
                        next_map,
                    )
                )
    if len(next_vals) == 0:
        return -np.inf
    else:
        print(max(next_vals))
        return max(next_vals)


def part1_old(fname="day23_input.txt"):
    with open(fname, "r") as f:
        lines = f.readlines()
        arr = np.zeros((len(lines), len(lines[0])-1))
        steppable = set()
        tried = set()
        trail = tuple([line[:-1] for line in lines])
        start = (0, 1)
        end = (len(lines)-1, len(lines[0])-3)
        # for i, line in enumerate(lines):
        #     for j, char in enumerate(line[:-1]):
        #         pass

        # keep trying paths, find the longest to the end
        return path_to_end(start, end, trail)


def part1(fname="day23_input.txt"):
    with open(fname, "r") as f:
        lines = f.readlines()
        trail = tuple([line[:-1] for line in lines])
        start = (0, 1)
        end = (len(lines)-1, len(lines[0])-3)

    longest = 0

    to_expand = [(start, trail, 0)]

    while len(to_expand) > 0:
        cur_node, cur_map, cur_step = to_expand.pop()
        if cur_node == end:
            longest = max(longest, cur_step)
            continue
        next_vals = []
        for offset in offsets:
            next_node = (cur_node[0] + offset[0], cur_node[1] + offset[1])
            if 0 <= next_node[0] < len(cur_map) and 0 <= next_node[1] < len(cur_map[0]):
                # print(next_node)
                if cur_map[next_node[0]][next_node[1]] == "#":
                    continue
                elif cur_map[next_node[0]][next_node[1]] == ">" and offset != (0, 1):
                    continue
                elif cur_map[next_node[0]][next_node[1]] == "<" and offset != (0, -1):
                    continue
                elif cur_map[next_node[0]][next_node[1]] == "v" and offset != (1, 0):
                    continue
                elif cur_map[next_node[0]][next_node[1]] == "^" and offset != (-1, 0):
                    continue
                next_map = []
                for i, line in enumerate(cur_map):
                    if i == next_node[0]:
                        next_map.append(block(line, next_node[1]))
                    else:
                        next_map.append(line)
                next_map = tuple(next_map)
                to_expand.append((next_node, next_map, cur_step + 1))

    return longest


def path_to_end(cur_map, cur, end):
    arr = np.zeros((len(cur_map), len(cur_map[0])))
    for i, row in enumerate(cur_map):
        for j, col in enumerate(row):
            if col != "#":
                arr[i, j] = 1
    labels, n = scipy.ndimage.label(arr)
    return labels[cur[0], cur[1]] == labels[end[0], end[1]]


def part2(fname="day23_input.txt"):
    with open(fname, "r") as f:
        lines = f.readlines()
        trail = tuple([line[:-1] for line in lines])
        start = (0, 1)
        end = (len(lines)-1, len(lines[0])-3)

    longest = 0

    to_expand = [(start, trail, 0)]
    # Note: another more efficient way might be to break it up by bottlenecks
    while len(to_expand) > 0:
        cur_node, cur_map, cur_step = to_expand.pop()
        if cur_node == end:
            longest = max(longest, cur_step)
            continue
        for offset in offsets:
            next_node = (cur_node[0] + offset[0], cur_node[1] + offset[1])
            if 0 <= next_node[0] < len(cur_map) and 0 <= next_node[1] < len(cur_map[0]):
                if cur_map[next_node[0]][next_node[1]] == "#":
                    continue
                if path_to_end(cur_map, next_node, end):
                    next_map = []
                    for i, line in enumerate(cur_map):
                        if i == next_node[0]:
                            next_map.append(block(line, next_node[1]))
                        else:
                            next_map.append(line)
                    next_map = tuple(next_map)
                    to_expand.append((next_node, next_map, cur_step + 1))

    return longest

# print(part1(fname="day23_test.txt"))
# print(part1(fname="day23_input.txt"))
# print(part2(fname="day23_test.txt"))
print(part2(fname="day23_input.txt"))
