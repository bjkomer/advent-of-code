def get_next(nums):
    diffs = []
    cur_list = nums
    while any(cur_list):
        next_nums = list()
        for i in range(len(cur_list)-1):
            next_nums.append(cur_list[i+1]-cur_list[i])
        diffs.append(next_nums)
        cur_list = next_nums

    total = 0
    for diff in diffs:
        total += diff[-1]
    return total + nums[-1]


def part1(fname="day9_input.txt"):
    total = 0
    with open(fname, "r") as f:
        lines = f.readlines()
        for line in lines:
            nums = [int(n) for n in line[:-1].split(" ")]
            total += get_next(nums)
    return total


def part2(fname="day9_input.txt"):
    total = 0
    with open(fname, "r") as f:
        lines = f.readlines()
        for line in lines:
            nums = [int(n) for n in line[:-1].split(" ")]
            total += get_next(list(reversed(nums)))
    return total


print(part1(fname="day9_test.txt"))
print(part1(fname="day9_input.txt"))
print(part2(fname="day9_test.txt"))
print(part2(fname="day9_input.txt"))
