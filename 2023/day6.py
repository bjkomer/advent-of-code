def part1(fname="day6_input.txt"):
    total = 1
    with open(fname, 'r') as f:
        lines = f.readlines()
        race_times = lines[0][:-1].split(" ")[1:]
        race_times = [int(rt) for rt in race_times if rt != ""]
        race_dists = lines[1][:-1].split(" ")[1:]
        race_dists = [int(rd) for rd in race_dists if rd != ""]
        for tt, td in zip(race_times, race_dists):
            count = 0
            for t in range(1, tt):
                if (tt-t)*t > td:
                    count += 1

            total *= count

    return total

def part2(fname="day6_input.txt"):
    total = 0
    with open(fname, 'r') as f:
        lines = f.readlines()
        race_times = lines[0][:-1].split(" ")[1:]
        race_times = [rt for rt in race_times if rt != ""]
        race_time = ""
        for rt in race_times:
            race_time += rt
        race_time = int(race_time)
        race_dists = lines[1][:-1].split(" ")[1:]
        race_dists = [rd for rd in race_dists if rd != ""]
        race_dist = ""
        for rd in race_dists:
            race_dist += rd
        race_dist = int(race_dist)
        for t in range(1, race_time):
            if (race_time-t)*t > race_dist:
                total += 1


    return total


print(part1("day6_test.txt"))
print(part1("day6_input.txt"))
print(part2("day6_test.txt"))
print(part2("day6_input.txt"))

