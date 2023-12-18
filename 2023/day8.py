import math

def part1(fname="day8_input.txt"):
    nodes = {}
    with open(fname, 'r') as f:
        lines = f.readlines()
        instructions = lines[0][:-1]
        for line in lines[2:]:
            nodes[line[:3]] = (line[7:10], line[12:15])
    cur = "AAA"
    count = 0
    while True:
        for d in instructions:
            if d == "L":
                cur = nodes[cur][0]
            else:
                cur = nodes[cur][1]
            count += 1
            if cur == "ZZZ":
                break
        else:
            continue
        break
    return count

def part2(fname="day8_input.txt"):
    nodes = {}
    with open(fname, 'r') as f:
        lines = f.readlines()
        instructions = lines[0][:-1]
        for line in lines[2:]:
            nodes[line[:3]] = (line[7:10], line[12:15])
    curs = [n for n in nodes.keys() if n[2] == "A"]
    loop_times = []
    for cur in curs:
        count = 0
        while True:
            for d in instructions:
                if d == "L":
                    cur = nodes[cur][0]
                else:
                    cur = nodes[cur][1]
                count += 1
                if cur[2] == "Z":
                    break
            else:
                continue
            break
        loop_times.append(count)
    return math.lcm(*loop_times)


print(part1("day8_test.txt"))
print(part1("day8_test2.txt"))
print(part1("day8_input.txt"))
print(part2("day8_test.txt"))
print(part2("day8_input.txt"))
