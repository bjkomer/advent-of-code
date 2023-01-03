def load_data(fname="day1_input.txt"):
    with open(fname) as f:
        lines = f.readlines()
        elf_index = 0
        elves = [[]]
        for line in lines:
            if line == "\n":
                elf_index += 1
                elves.append([])
            else:
                elves[elf_index].append(int(line))
    return elves


def part1():
    elves = load_data(fname="day1_input.txt")
    max_cal = 0
    for elf in elves:
        max_cal = max(max_cal, sum(elf))
    return max_cal


def part2():
    elves = load_data(fname="day1_input.txt")
    cals = []
    for elf in elves:
        cals.append(sum(elf))
    return sum(sorted(cals)[-3:])


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")

