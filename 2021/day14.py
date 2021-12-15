from collections import defaultdict
from functools import lru_cache


def get_data():

    insertion = defaultdict(lambda: '')
    with open("day14_input.txt", "r") as f:
        lines = f.readlines()
        start = lines[0][:-1]
        for line in lines[2:]:
            a, b = line[:-1].split(" -> ")
            insertion[a] = b
    return start, insertion

def apply_insert(base, insertion):
    # go backwards so there is no need to worry about the length changing
    for i in range(len(base)-2, -1, -1):
        if base[i] + base[i+1] in insertion.keys():
            base = base[:i+1] + insertion[base[i] + base[i+1]] + base[i+1:]
    return base

def make_independent(base, insertion):
    seg_dict = defaultdict(lambda: 0)
    start = 0
    end = 1
    while end < len(base):
        if base[start] + base[end] in insertion.keys():
            end += 1
        else:
            print("found a split!")
            seg_dict[base[start:end]] += 1
            start = end
            end = start + 1
    else:
        seg_dict[base[start:end]] += 1  # attach the leftover string
    return seg_dict


def apply_seg_insert(seg, insertion):
    new_seg = defaultdict(lambda: 0)
    for base, count in seg.items():
        base = apply_insert(base, insertion)
        cur_seg = make_independent(base, insertion)
        for k, v in cur_seg.items():
            new_seg[k] += count
    return new_seg


def part1(steps=10):
    base, insertion = get_data()
    for i in range(steps):
        base = apply_insert(base, insertion)
    counts = defaultdict(lambda: 0)
    for char in base:
        counts[char] += 1
    max_count = 0
    min_count = float("inf")
    for char, count in counts.items():
        max_count = max(max_count, count)
        min_count = min(min_count, count)
    return max_count - min_count

def part2_brute_force(steps=40):
    # split the string on connections that have no insertion
    # keep counts of duplicate segments, solve them only once each step
    base, insertion = get_data()
    seg = make_independent(base, insertion)
    for i in range(steps):
        print(i)
        seg = apply_seg_insert(seg, insertion)
    
    counts = defaultdict(lambda: 0)
    for chars, count in seg.items():
        for char in chars:
            counts[char] += count  # increase total count by the number of copies
    max_count = 0
    min_count = float("inf")
    for char, count in counts.items():
        max_count = max(max_count, count)
        min_count = min(min_count, count)
    return max_count - min_count


def part2_recursive(steps=40):
    base, insertion = get_data()
    @lru_cache
    def fill_in(first, second, steps):
        if steps == 1:
            return insertion[first + second]
        else:
            return fill_in(first, insertion[first + second], steps - 1) + insertion[first + second] + fill_in(insertion[first+second], second, steps - 1)
    out_str = ''
    for i in range(len(base)-1):
        out_str += base[i] + fill_in(base[i], base[i+1], steps=steps)
    out_str += base[-1]
    
    counts = defaultdict(lambda: 0)
    for char in out_str:
        counts[char] += 1
    max_count = 0
    min_count = float("inf")
    for char, count in counts.items():
        max_count = max(max_count, count)
        min_count = min(min_count, count)
    return max_count - min_count

def part2(steps=40):
    # only care about the pair counts, don't build the actual string
    base, insertion = get_data()
    pair_counts = defaultdict(lambda: 0)
    counts = defaultdict(lambda: 0)
    # initialize pair counts
    for i in range(len(base)-1):
        pair_counts[base[i]+base[i+1]] += 1
        counts[base[i]] += 1
    counts[base[-1]] += 1

    for i in range(steps):
        next_pair_counts = defaultdict(lambda: 0)
        for k, v in pair_counts.items():
            ins = insertion[k]
            counts[ins] += v
            next_pair_counts[k[0] + ins] += v
            next_pair_counts[ins + k[1]] += v
        pair_counts = next_pair_counts.copy()

    max_count = 0
    min_count = float("inf")
    for char, count in counts.items():
        max_count = max(max_count, count)
        min_count = min(min_count, count)
    return max_count - min_count

print(part1(steps=10))
print(part2(steps=40))

