from functools import lru_cache


@lru_cache
def possibilities(record, sizes):
    if len(record) == 0:
        if len(sizes) > 0:
            return 0
        else:
            return 1
    if len(sizes) == 0:
        if "#" in record:
            return 0
        else:
            return 1
    next_size = sizes[0]
    # get first '?' or '#' and see if it fits
    for i, char in enumerate(record):
        if char == "#":
            if len(record[i:]) == next_size and "." not in record[i:i+next_size]:
                # valid, must use
                return possibilities(record[i+next_size:], sizes[1:])
            elif len(record[i:]) > next_size and "." not in record[i:i+next_size] and record[i+next_size] != "#":
                # valid, must use
                return possibilities(record[i+next_size+1:], sizes[1:])
            else:
                return 0
        elif char == "?":
            if len(record[i:]) == next_size and "." not in record[i:i+next_size]:
                return possibilities(record[i+next_size:], sizes[1:]) + possibilities(record[i+1:], sizes)
            elif len(record[i:]) > next_size and "." not in record[i:i+next_size] and record[i+next_size] != "#":
                return possibilities(record[i+next_size+1:], sizes[1:]) + possibilities(record[i+1:], sizes)
            else:
                return possibilities(record[i+1:], sizes)
    return 0


def part1(fname="day12_input.txt"):
    total = 0
    with open(fname, "r") as f:
        lines = f.readlines()
        for line in lines:
            record, sizes = line[:-1].split(" ")
            sizes = tuple([int(s) for s in sizes.split(",")])
            total += possibilities(record, sizes)
    return total


def part2(fname="day12_input.txt"):
    total = 0
    with open(fname, "r") as f:
        lines = f.readlines()
        for line in lines:
            base_record, base_sizes = line[:-1].split(" ")
            record = base_record
            sizes = base_sizes
            for _ in range(4):
                record = record + "?" + base_record
                sizes = sizes + "," + base_sizes
            sizes = tuple([int(s) for s in sizes.split(",")])
            total += possibilities(record, sizes)
    return total


print(part1(fname="day12_test.txt"))
print(part1(fname="day12_input.txt"))
print(part2(fname="day12_test.txt"))
print(part2(fname="day12_input.txt"))
