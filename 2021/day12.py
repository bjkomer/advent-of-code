from collections import defaultdict
import string

def get_data():
    conn = defaultdict(lambda: [])
    with open("day12_input.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            a, b = line[:-1].split("-")
            # Do not connect back to the start, to make part 2 code simpler
            if b != "start":
                conn[a].append(b)
            if a != "start":
                conn[b].append(a)
    return conn

def count_paths(cur, conn, visited, double_used=True):
    if cur == "end":
        return 1
    count = 0
    if cur[0] in string.ascii_lowercase: # if lowercase, cannot visit it again
        visited.append(cur)
    for cave in conn[cur]:
        if cave not in visited:  # do not go to small caves twice
            new_visited = visited.copy()
            count += count_paths(cave, conn, new_visited, double_used=double_used)
        elif not double_used:
            new_visited = visited.copy()
            count += count_paths(cave, conn, new_visited, double_used=True)
    return count


def solve(double_used=True):
    conn = get_data()
    visited = []
    return count_paths(cur="start", conn=conn, visited=visited, double_used=double_used)


print(solve(double_used=True))  # Part 1
print(solve(double_used=False))  # Part 2

