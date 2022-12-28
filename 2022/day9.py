import numpy as np
import math


def parse_input(fname="day9_input.txt"):
    with open(fname, "r") as f:
        lines = f.readlines()
        commands = np.zeros((len(lines), 2), dtype=np.int32)
        for i, line in enumerate(lines):
            if line[0] == "U":
                commands[i, 0] = int(line.strip()[2:])
            elif line[0] == "D":
                commands[i, 0] = -int(line.strip()[2:])
            elif line[0] == "L":
                commands[i, 1] = -int(line.strip()[2:])
            elif line[0] == "R":
                commands[i, 1] = int(line.strip()[2:])
            else:
                raise NotImplementedError
    return commands


def update_tail(cur_head, cur_tail):

    if cur_head == cur_tail:
        return cur_tail
    elif cur_head[0] == cur_tail[0]:
        if cur_head[1] > cur_tail[1]:
            return (cur_tail[0], cur_head[1] - 1)
        else:
            return (cur_tail[0], cur_head[1] + 1)
    elif cur_head[1] == cur_tail[1]:
        if cur_head[0] > cur_tail[0]:
            return (cur_head[0] - 1, cur_tail[1])
        else:
            return (cur_head[0] + 1, cur_tail[1])
    else:  # Diagonal case
        diff = np.array(cur_head) - np.array(cur_tail)
        if abs(diff[0]) == 1 and abs(diff[1]) == 1:
            return cur_tail  # touching diagonally, so don't move
        else:
            return (cur_tail[0] + np.sign(diff[0]), cur_tail[1] + np.sign(diff[1]))


def part1(fname="day9_input.txt"):
    commands = parse_input(fname=fname)

    cur_head = (0, 0)
    cur_tail = (0, 0)
    heads = {(0, 0): True}
    tails = {(0, 0): True}

    for command in commands:
        if command[0] > 0:
            for _ in range(command[0]):
                cur_head = (cur_head[0] + 1, cur_head[1])
                cur_tail = update_tail(cur_head, cur_tail)
                tails[cur_tail] = True
        elif command[0] < 0:
            for _ in range(-command[0]):
                cur_head = (cur_head[0] - 1, cur_head[1])
                cur_tail = update_tail(cur_head, cur_tail)
                tails[cur_tail] = True
        elif command[1] > 0:
            for _ in range(command[1]):
                cur_head = (cur_head[0], cur_head[1] + 1)
                cur_tail = update_tail(cur_head, cur_tail)
                tails[cur_tail] = True
        elif command[1] < 0:
            for _ in range(-command[1]):
                cur_head = (cur_head[0], cur_head[1] - 1)
                cur_tail = update_tail(cur_head, cur_tail)
                tails[cur_tail] = True

    return len(tails.keys())


def update_knots(cur_knot):
    for k in range(1, 10):
        cur_knot[k] = update_tail(cur_knot[k-1], cur_knot[k])


def part2(fname="day9_input.txt"):
    commands = parse_input(fname=fname)

    cur_knot = [(0, 0) for _ in range(10)]

    tails = {(0, 0): True}

    for command in commands:
        if command[0] > 0:
            for _ in range(command[0]):
                cur_knot[0] = (cur_knot[0][0] + 1, cur_knot[0][1])
                update_knots(cur_knot)
                tails[cur_knot[-1]] = True
        elif command[0] < 0:
            for _ in range(-command[0]):
                cur_knot[0] = (cur_knot[0][0] - 1, cur_knot[0][1])
                update_knots(cur_knot)
                tails[cur_knot[-1]] = True
        elif command[1] > 0:
            for _ in range(command[1]):
                cur_knot[0] = (cur_knot[0][0], cur_knot[0][1] + 1)
                update_knots(cur_knot)
                tails[cur_knot[-1]] = True
        elif command[1] < 0:
            for _ in range(-command[1]):
                cur_knot[0] = (cur_knot[0][0], cur_knot[0][1] - 1)
                update_knots(cur_knot)
                tails[cur_knot[-1]] = True

    return len(tails.keys())


print(part1())
print(part2())
