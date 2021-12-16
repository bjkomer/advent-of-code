import numpy as np
import heapq

def get_data(full_map):

    with open("day15_input.txt", "r") as f:
        lines = f.readlines()
        height = len(lines)
        width = len(lines[0]) - 1
        arr = np.zeros((height, width), dtype=np.int32)
        for i, line in enumerate(lines):
            for j, char in enumerate(line[:-1]):
                arr[i, j] = int(char)
    if full_map:
        large_arr = np.zeros((height * 5, width * 5), dtype=np.int32)
        for i in range(5):
            for j in range(5):
                large_arr[i*height:(i+1)*height, j*width:(j+1)*width] = arr + i + j
        large_arr[large_arr>9] -= 9  # do wrapping
        return large_arr
    else:
        return arr


def solve(full_map=False):
    arr = get_data(full_map)
    h = []
    # priority (total cost plus estimate), total cost, x index, y index
    height = arr.shape[0]
    width = arr.shape[1]
    costs = np.ones_like(arr, dtype=np.int32) * height * width * 9  # initialize to largest value
    # start from the end
    i = arr.shape[0] - 1
    j = arr.shape[1] - 1
    heapq.heappush(h, (arr[-1, -1] + i + j, arr[-1, -1], i, j))

    while len(h) > 0:
        cur = heapq.heappop(h)
        cost = cur[1]
        x = cur[2]
        y = cur[3]
        if x == 0 and y == 0:
            return cost - arr[0, 0]
        for i, j in zip([x + 1, x - 1, x, x], [y, y, y + 1, y - 1]):
            if 0 <= i < height and 0 <= j < width:
                travel_cost = cost + arr[i, j]
                if travel_cost < costs[i, j]:
                    costs[i, j] = travel_cost
                    heapq.heappush(h, (costs[i, j] + i + j, costs[i, j], i, j))

print(solve(full_map=False))  # Part 1
print(solve(full_map=True))  # Part 2

