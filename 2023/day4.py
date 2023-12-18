import numpy as np

def get_nums(num_str):
    return [int(num) for num in num_str.split(" ") if len(num) > 0]

def part1(fname="day4_input.txt"):
    total = 0
    with open(fname, 'r') as f:
        lines = f.readlines()
        for line in lines:
            sets = line[:-1].split(":")[1]
            win_str, num_str = sets.split(" | ")
            win = get_nums(win_str)
            num = get_nums(num_str)
            points = 0
            for w in win:
                if w in num:
                    if points == 0:
                        points = 1
                    else:
                        points *= 2

            total += points

    return total

def num_wins(line):
    sets = line[:-1].split(":")[1]
    win_str, num_str = sets.split(" | ")
    win = get_nums(win_str)
    num = get_nums(num_str)
    points = 0
    for w in win:
        if w in num:
            points += 1
    return points

def part2(fname="day4_input.txt"):
    total = 0
    with open(fname, 'r') as f:
        lines = f.readlines()
        card_array = np.ones((len(lines),), dtype=np.int32)
        for i, line in enumerate(lines):
            n_wins = num_wins(line)
            card_array[i+1:i+n_wins+1] += card_array[i]
    return card_array.sum()


print(part1("day4_test.txt"))
print(part1("day4_input.txt"))
print(part2("day4_test.txt"))
print(part2("day4_input.txt"))
