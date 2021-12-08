import numpy as np


with open("day7_input.txt", "r") as f:
    pos = np.array([int(x) for x in f.readline()[:-1].split(",")])


def get_fuel(final_pos, constant=True):
    fuel = 0
    for p in pos:
        if constant:
            fuel += abs(p - final_pos)
        else:
            diff = abs(p - final_pos)
            fuel += (diff * (diff+1)) // 2  # make a triangle
    return fuel

def solve_brute_force(constant=True):

    n_crabs = len(pos)
    min_pos = np.min(pos)
    max_pos = np.max(pos)

    best_fuel = np.inf
    for check in range(min_pos, max_pos + 1):
        best_fuel = min(best_fuel, get_fuel(check, constant=constant))
    return best_fuel

def solve_fast(constant=True):

    if constant:
        check_up = int(np.ceil(np.median(pos)))
        check_down = int(np.floor(np.median(pos)))
    else:
        check_up = int(np.ceil(np.mean(pos)))
        check_down = int(np.floor(np.mean(pos)))
    
    return min(get_fuel(check_down, constant=constant), get_fuel(check_up, constant=constant))

print(solve_fast(constant=True))  # Part 1
print(solve_fast(constant=False))  # Part 2

print(solve_brute_force(constant=True))  # Part 1
print(solve_brute_force(constant=False))  # Part 2

