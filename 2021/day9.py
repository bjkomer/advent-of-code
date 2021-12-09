import numpy as np
from functools import reduce

def load_data():
    with open("day9_input.txt", "r") as f:
        lines = f.readlines()
        length = len(lines)
        width = len(lines[0]) - 1  # -1 to ignore the newline character
        # initialize the array slightly larger with a wall of 10s so no need for special boundary checks
        arr = np.ones((length + 2, width + 2), dtype=np.int32) * 10
        for i, line in enumerate(lines):
            for j, char in enumerate(line[:-1]):
                arr[i + 1, j + 1] = int(char)

    return arr, length, width


def part1():
    arr, length, width = load_data()

    risk = 0
    for i in range(1, length + 1):
        for j in range(1, width + 1):
            # check if lower than adjacent locations
            if arr[i, j] < arr[i + 1, j] and arr[i, j] < arr[i - 1, j] and arr[i, j] < arr[i, j + 1] and arr[i, j] < arr[i, j - 1]:
                risk += arr[i, j] + 1

    return risk



def fill_basin(x, y, arr):
    if arr[x, y] >= 9:
        return 0

    arr[x, y] = 10  # fill it in so it won't get checked again
    return 1 + fill_basin(x+1,y,arr) + fill_basin(x-1,y,arr) + fill_basin(x,y+1,arr) + fill_basin(x,y-1,arr)

def part2():
    # just need to find the regions split by 9s
    arr, length, width = load_data()
    
    sizes = []
    for i in range(1, length + 1):
        for j in range(1, width + 1):
            size = fill_basin(i, j, arr)
            if size > 0:
                sizes.append(size)

    # return the product of the three largest sizes found
    return reduce(lambda x, y: x * y, sorted(sizes)[-3:])


print(part1())
print(part2())

