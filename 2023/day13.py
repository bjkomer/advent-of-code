def x_mirror(dist, gather):
    check_len = min(dist+1, len(gather) - dist - 1)

    for i in range(check_len):
        if tuple(gather[dist - i]) != tuple(gather[dist + i + 1]):
            return False
    return True


def y_mirror(dist, gather):
    check_len = min(dist+1, len(gather[0]) - dist - 1)
    for line in gather:
        for i in range(check_len):
            if line[dist - i] != line[dist + i + 1]:
                return False
    return True


def x_mirror_smudge(dist, gather):
    check_len = min(dist+1, len(gather) - dist - 1)
    diff_count = 0
    for i in range(check_len):
        for j in range(len(gather[dist - i])):
            if gather[dist - i][j] != gather[dist + i + 1][j]:
                diff_count += 1
                if diff_count >= 2:
                    return False
    return diff_count == 1


def y_mirror_smudge(dist, gather):
    diff_count = 0
    check_len = min(dist+1, len(gather[0]) - dist - 1)
    for line in gather:
        for i in range(check_len):
            if line[dist - i] != line[dist + i + 1]:
                diff_count += 1
                if diff_count >= 2:
                    return False
    return diff_count == 1


def score(gather):
    x_max = len(gather)
    y_max = len(gather[0])
    for i in range(x_max-1):
        if x_mirror(i, gather):
            return 100*(i+1)
    for i in range(y_max-1):
        if y_mirror(i, gather):
            return i+1


def score_smudge(gather):
    x_max = len(gather)
    y_max = len(gather[0])
    for i in range(x_max-1):
        if x_mirror_smudge(i, gather):
            return 100*(i+1)
    for i in range(y_max-1):
        if y_mirror_smudge(i, gather):
            return i+1


def part1(fname="day13_input.txt"):
    total = 0
    with open(fname, "r") as f:
        lines = f.readlines()
        gather = []
        for line in lines:
            if line == "\n":
                total += score(gather)
                gather = []
            else:
                gather.append(line[:-1])
        else:
            total += score(gather)
    return total


def part2(fname="day13_input.txt"):
    total = 0
    with open(fname, "r") as f:
        lines = f.readlines()
        gather = []
        for line in lines:
            if line == "\n":
                total += score_smudge(gather)
                gather = []
            else:
                gather.append(line[:-1])
        else:
            total += score(gather)
    return total


print(part1(fname="day13_test.txt"))
print(part1(fname="day13_input.txt"))
print(part2(fname="day13_test.txt"))
print(part2(fname="day13_input.txt"))
