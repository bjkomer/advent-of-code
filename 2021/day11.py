import numpy as np

def load_data():
    arr = np.zeros((10,10))
    with open("day11_input.txt", "r") as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            for j, char in enumerate(line[:-1]):
                arr[i, j] = int(char)
    return arr

def update(i, j, last_flashed, total_flashed, arr):
    arr[i, j] += 1
    if arr[i, j] > 9 and total_flashed[i, j] == 0:
        last_flashed[i, j] = 1
        total_flashed[i, j] = 1


def add_energy(last_flashed, total_flashed, arr):
    inds = np.where(last_flashed==1)
    last_flashed[:] = 0  # zero out to fill in with new flashes
    for i, j in zip(*inds):
        # check the 8 adjacent octopodes
        if (i + 1) < 10 and (j + 1) < 10:
            update(i + 1, j + 1, last_flashed, total_flashed, arr)
        if (i + 1) < 10:
            update(i + 1, j, last_flashed, total_flashed, arr)
        if (i + 1) < 10 and (j - 1) >= 0:
            update(i + 1, j - 1, last_flashed, total_flashed, arr)
        if (i - 1) >= 0 and (j + 1) < 10:
            update(i - 1, j + 1, last_flashed, total_flashed, arr)
        if (i - 1) >= 0:
            update(i - 1, j, last_flashed, total_flashed, arr)
        if (i - 1) >= 0 and (j - 1) >= 0:
            update(i - 1, j - 1, last_flashed, total_flashed, arr)
        if (j + 1) < 10:
            update(i, j + 1, last_flashed, total_flashed, arr)
        if (j - 1) >= 0:
            update(i, j - 1, last_flashed, total_flashed, arr)


def simulate(arr):
    total_flashed = np.zeros_like(arr)  # all the octopi that flashed this step
    last_flashed = np.zeros_like(arr)  # the octopuses that flashed on the last check
    # increase energy of every octopus
    arr += 1
    total_flashed[np.where(arr>9)] = 1
    last_flashed[np.where(arr>9)] = 1
    while np.sum(last_flashed) > 0:  # simulate this step until no more octopice flash
        # add energy around each recent flash
        add_energy(last_flashed, total_flashed, arr)
    # reset any flashed octopeese
    arr[np.where(arr>9)] = 0
    return np.sum(total_flashed)

def part1(steps=100):
    arr = load_data()
    flashes = 0
    for step in range(steps):
        flashes += simulate(arr)
    return int(flashes)

def part2():
    arr = load_data()
    step = 0
    while True:
        step += 1
        simulate(arr)
        if np.sum(arr) == 0:  # all octopen flashed at the same time
            break
    return step

print(part1())
print(part2())

