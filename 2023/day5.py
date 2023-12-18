import numpy as np

def part1(fname="day5_input.txt"):
    mapping = {
            "seed-to-soil":[],
            "soil-to-fertilizer": [],
            "fertilizer-to-water": [],
            "water-to-light": [],
            "light-to-temperature": [],
            "temperature-to-humidity": [],
            "humidity-to-location": [],
    }
    cur_map = ""
    with open(fname, 'r') as f:
        lines = f.readlines()
        seeds = lines[0][7:-1].split(" ")
        for line in lines[1:]:
            if line[:-1] == "":
                continue
            elif "map" in line:
                cur_map = line.split(" ")[0]
            else:
                nums = line[:-1].split(" ")
                first = int(nums[0])
                second = int(nums[1])
                count = int(nums[2])
                mapping[cur_map].append([second, first, count])
        best = np.inf
        for seed in seeds:
            print("")
            loc = int(seed)
            for m in ["seed-to-soil", "soil-to-fertilizer", "fertilizer-to-water", "water-to-light", "light-to-temperature", "temperature-to-humidity", "humidity-to-location"]:
                for mp in mapping[m]:
                    if (mp[0] <= loc) and (loc < mp[0] + mp[2]):
                        diff = loc - mp[0]
                        loc = mp[1] + diff
                        break
            if int(loc) < best:
                best = int(loc)
    return best

def get_seed_for_loc(loc, mapping):
    seed = int(loc)
    for m in reversed(["seed-to-soil", "soil-to-fertilizer", "fertilizer-to-water", "water-to-light", "light-to-temperature", "temperature-to-humidity", "humidity-to-location"]):
        for mp in mapping[m]:
            if (mp[1] <= seed) and (seed < mp[1] + mp[2]):
                diff = seed - mp[1]
                seed = mp[0] + diff
                break
    return seed


def part2(fname="day5_input.txt"):
    # do it backwards
    mapping = {
            "seed-to-soil":[],
            "soil-to-fertilizer": [],
            "fertilizer-to-water": [],
            "water-to-light": [],
            "light-to-temperature": [],
            "temperature-to-humidity": [],
            "humidity-to-location": [],
    }
    cur_map = ""
    best = np.inf
    with open(fname, 'r') as f:
        lines = f.readlines()
        fake_seeds = lines[0][7:-1].split(" ")
        seeds = []
        for line in lines[1:]:
            if line[:-1] == "":
                continue
            elif "map" in line:
                cur_map = line.split(" ")[0]
            else:
                nums = line[:-1].split(" ")
                first = int(nums[0])
                second = int(nums[1])
                count = int(nums[2])
                mapping[cur_map].append([second, first, count])
        for s in range(100000000):
            seed = get_seed_for_loc(s, mapping)
            for i in range(len(fake_seeds)//2):
                if int(fake_seeds[i*2]) <= int(seed) <= int(fake_seeds[i*2]) + int(fake_seeds[i*2+1]):
                    return s



print(part1("day5_test.txt"))
print(part1("day5_input.txt"))
print(part2("day5_test.txt"))
print(part2("day5_input.txt"))
