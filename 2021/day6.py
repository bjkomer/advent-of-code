from collections import defaultdict


with open("day6_input.txt", "r") as f:
    ages = [int(x) for x in f.readline()[:-1].split(",")]


def simulate(population):
    new_population = defaultdict(lambda: 0)

    new_population[8] = population[0]  # new fish
    new_population[6] = population[0]  # old fish resetting
    for age in range(1, 9):
        new_population[age-1] += population[age]  # aging

    return new_population


def solve(days=80):
    # keep track of the number of fish at each age
    population = defaultdict(lambda: 0)

    # initialize population
    for age in ages:
        population[age] += 1

    for day in range(days):
        population = simulate(population)

    n_fish = 0
    for age in range(9):
        n_fish += population[age]

    return n_fish

print(solve(days=80))  # part 1
print(solve(days=256))  # part 2

