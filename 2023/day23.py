import numpy as np
from functools import lru_cache
from collections import defaultdict
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
    if start == end:
        return 0
    next_vals = []
    for offset in offsets:
        next_node = (start[0] + offset[0], start[1] + offset[1])
        if 0 <= next_node[0] < len(cur_map) and 0 <= next_node[1] < len(cur_map[0]):
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


def part1_recursive(fname="day23_input.txt"):
    with open(fname, "r") as f:
        lines = f.readlines()
        trail = tuple([line[:-1] for line in lines])
        start = (0, 1)
        end = (len(lines)-1, len(lines[0])-3)

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


def part2_slow(fname="day23_input.txt"):
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


def get_longest_path(start, end, cur_map):
    longest = 0

    to_expand = [(start, cur_map, 0)]
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


def opposite(node):
    return -node[0], -node[1]


def part2(fname="day23_input.txt"):
    with open(fname, "r") as f:
        lines = f.readlines()
        trail = tuple([line[:-1] for line in lines])
        start = (0, 1)
        end = (len(lines)-1, len(lines[0])-3)

    # find all of the junction points
    tried = set()
    junctions = set()
    junctions.add(start)
    junctions.add(end)
    to_expand = [(start, start, (1, 0), (1, 0))]
    connections = {}

    while len(to_expand) > 0:
        cur_node, last_junction, last_move, initial_junction_move = to_expand.pop()
        if cur_node == end:
            connections[(last_junction, end)] = (initial_junction_move, last_move)
            continue
        next_nodes = []
        valid_offsets = []
        for offset in offsets:
            next_node = (cur_node[0] + offset[0], cur_node[1] + offset[1])
            if 0 <= next_node[0] < len(trail) and 0 <= next_node[1] < len(trail[0]):
                if trail[next_node[0]][next_node[1]] == "#":
                    continue
                else:
                    next_nodes.append(next_node)
                    valid_offsets.append(offset)
        is_junction = len(next_nodes) >= 3
        if is_junction:
            connections[(last_junction, cur_node)] = (initial_junction_move, last_move)
            connections[(cur_node, last_junction)] = (opposite(last_move), opposite(initial_junction_move))
            junctions.add(cur_node)
        else:
            tried.add(cur_node)

        for i, next_node in enumerate(next_nodes):
            if (next_node in junctions or next_node not in tried) and valid_offsets[i] != opposite(last_move):
                if is_junction:
                    to_expand.append((next_node, cur_node, valid_offsets[i], valid_offsets[i]))
                else:
                    to_expand.append((next_node, last_junction, valid_offsets[i], initial_junction_move))

    longest_paths = {}
    neighbours = defaultdict(lambda: set())
    for pair, directions in connections.items():
        p_start = pair[0]
        p_end = pair[1]
        init_move = directions[0]

        next_map = []
        for i, line in enumerate(trail):
            if i == p_start[0]:
                next_map.append(block(line, p_start[1]))
            else:
                next_map.append(line)

        lp = 1 + get_longest_path(
            (p_start[0] + init_move[0], p_start[1] + init_move[1]),
            p_end,
            tuple(next_map)
        )
        longest_paths[pair] = lp

        neighbours[p_start].add((p_end, lp))
        neighbours[p_end].add((p_start, lp))

    longest = 0

    to_expand = [(start, 0, set(start))]

    while len(to_expand) > 0:
        cur_node, distance, cur_tried = to_expand.pop()
        if cur_node == end:
            longest = max(longest, distance)
            continue
        else:
            for neighbour in neighbours[cur_node]:
                if neighbour[0] not in cur_tried:
                    next_tried = cur_tried.copy()
                    next_tried.add(neighbour[0])
                    to_expand.append((neighbour[0], distance + neighbour[1], next_tried))

    return longest


print(part1(fname="day23_test.txt"))
print(part1(fname="day23_input.txt"))
print(part2(fname="day23_test.txt"))
print(part2(fname="day23_input.txt"))
