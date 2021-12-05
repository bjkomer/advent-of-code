from collections import defaultdict


def parse_line(line):
    a, b = line.split(" -> ")
    x1, y1 = a.split(",")
    x2, y2 = b[:-1].split(",")  # trim off the newline before splitting
    return int(x1), int(y1), int(x2), int(y2)

def solve(part=1):
    # all points that a line crosses
    points = defaultdict(lambda: 0)

    n_overlap = 0

    # Parsing File
    with open("day5_input.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            x1, y1, x2, y2 = parse_line(line)
            # only count vertical and horizontal lines for part 1
            if x1 == x2:
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    points[(x1, y)] += 1
                    if points[(x1, y)] == 2:
                        n_overlap += 1
            elif y1 == y2:
                for x in range(min(x1, x2), max(x1, x2) + 1):
                    points[(x, y1)] += 1
                    if points[(x, y1)] == 2:
                        n_overlap += 1
            elif part == 2:
                dist = abs(x2 - x1)
                dirx = (x2 - x1) // dist
                diry = (y2 - y1) // dist
                for d in range(dist + 1):
                    x = x1 + d * dirx
                    y = y1 + d * diry
                    points[(x, y)] += 1
                    if points[(x, y)] == 2:
                        n_overlap += 1

    return n_overlap


print(solve(part=1))
print(solve(part=2))

