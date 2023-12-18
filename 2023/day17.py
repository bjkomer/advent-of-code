import numpy as np
from functools import lru_cache
from collections import defaultdict
from heapq import heappush, heappop, heapify

# Constants for how many moves have been used in a direction
R1 = 0
R2 = 1
R3 = 2
L1 = 3
L2 = 4
L3 = 5
D1 = 6
D2 = 7
D3 = 8
U1 = 9
U2 = 10
U3 = 11


Rs = 0
Re = 9
Ls = 10
Le = 19
Ds = 20
De = 29
Us = 30
Ue = 39


def heuristic(node):
    return 9*(node[0]+node[1])


def get_neighbours(node):
    connected = []
    if R1 <= node[2] <= R3:
        connected.append((node[0] + 1, node[1], D1))
        connected.append((node[0] - 1, node[1], U1))
        if node[2] != R3:
            connected.append((node[0], node[1] + 1, node[2] + 1))
    if L1 <= node[2] <= L3:
        connected.append((node[0] + 1, node[1], D1))
        connected.append((node[0] - 1, node[1], U1))
        if node[2] != L3:
            connected.append((node[0], node[1] - 1, node[2] + 1))
    if D1 <= node[2] <= D3:
        connected.append((node[0], node[1] + 1, R1))
        connected.append((node[0], node[1] - 1, L1))
        if node[2] != D3:
            connected.append((node[0] + 1, node[1], node[2] + 1))
    if U1 <= node[2] <= U3:
        connected.append((node[0], node[1] + 1, R1))
        connected.append((node[0], node[1] - 1, L1))
        if node[2] != U3:
            connected.append((node[0] - 1, node[1], node[2] + 1))

    return connected


def get_neighbours_ultra(node):
    connected = []
    if Rs <= node[2] <= Re:
        if node[2] % 10 >= 3:
            connected.append((node[0] + 1, node[1], Ds))
            connected.append((node[0] - 1, node[1], Us))
        if node[2] != Re:
            connected.append((node[0], node[1] + 1, node[2] + 1))
    if Ls <= node[2] <= Le:
        if node[2] % 10 >= 3:
            connected.append((node[0] + 1, node[1], Ds))
            connected.append((node[0] - 1, node[1], Us))
        if node[2] != Le:
            connected.append((node[0], node[1] - 1, node[2] + 1))
    if Ds <= node[2] <= De:
        if node[2] % 10 >= 3:
            connected.append((node[0], node[1] + 1, Rs))
            connected.append((node[0], node[1] - 1, Ls))
        if node[2] != De:
            connected.append((node[0] + 1, node[1], node[2] + 1))
    if Us <= node[2] <= Ue:
        if node[2] % 10 >= 3:
            connected.append((node[0], node[1] + 1, Rs))
            connected.append((node[0], node[1] - 1, Ls))
        if node[2] != Ue:
            connected.append((node[0] - 1, node[1], node[2] + 1))

    return connected


def part1(fname="day17_input.txt"):
    with open(fname, "r") as f:
        lines = f.readlines()
        heat = np.zeros((len(lines), len(lines[0])-1))
        for i, line in enumerate(lines):
            for j, char in enumerate(line[:-1]):
                heat[i, j] = int(char)

    costs = defaultdict(lambda: np.inf)
    goal_x = heat.shape[0] - 1
    goal_y = heat.shape[1] - 1
    costs[(0, 0, R1)] = 0
    costs[(0, 0, D1)] = 0
    to_expand = []
    heappush(to_expand, (0, (0, 0, R1)))
    heappush(to_expand, (0, (0, 0, D1)))

    while(len(to_expand)) > 0:
        _, cur_node = heappop(to_expand)

        if cur_node[0] == goal_x and cur_node[1] == goal_y:
            return costs[cur_node]

        neighbours = get_neighbours(cur_node)
        for neighbour in neighbours:
            if 0 <= neighbour[0] <= goal_x and 0 <= neighbour[1] <= goal_y:
                new_cost = costs[cur_node] + heat[neighbour[0], neighbour[1]]
                if new_cost < costs[neighbour]:
                    costs[neighbour] = new_cost
                    heappush(to_expand, (new_cost + heuristic(neighbour), neighbour))


def part2(fname="day17_input.txt"):
    with open(fname, "r") as f:
        lines = f.readlines()
        heat = np.zeros((len(lines), len(lines[0])-1))
        for i, line in enumerate(lines):
            for j, char in enumerate(line[:-1]):
                heat[i, j] = int(char)

    costs = defaultdict(lambda: np.inf)
    goal_x = heat.shape[0] - 1
    goal_y = heat.shape[1] - 1
    costs[(0, 0, R1)] = 0
    costs[(0, 0, D1)] = 0
    to_expand = []
    heappush(to_expand, (0, (0, 0, R1)))
    heappush(to_expand, (0, (0, 0, D1)))

    while(len(to_expand)) > 0:
        _, cur_node = heappop(to_expand)

        if cur_node[0] == goal_x and cur_node[1] == goal_y and cur_node[2] % 10 >= 3:
            return costs[cur_node]

        neighbours = get_neighbours_ultra(cur_node)
        for neighbour in neighbours:
            if 0 <= neighbour[0] <= goal_x and 0 <= neighbour[1] <= goal_y:
                new_cost = costs[cur_node] + heat[neighbour[0], neighbour[1]]
                if new_cost < costs[neighbour]:
                    costs[neighbour] = new_cost
                    heappush(to_expand, (new_cost + heuristic(neighbour), neighbour))


print(part1(fname="day17_test.txt"))
print(part1(fname="day17_input.txt"))
print(part2(fname="day17_test.txt"))
print(part2(fname="day17_test2.txt"))
print(part2(fname="day17_input.txt"))
