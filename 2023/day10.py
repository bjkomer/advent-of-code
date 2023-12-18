connections = {
    "L": [(-1, 0), (0, 1)],
    "F": [(1, 0), (0, 1)],
    "J": [(-1, 0), (0, -1)],
    "7": [(1, 0), (0, -1)],
    "|": [(1, 0), (-1, 0)],
    "-": [(0, 1), (0, -1)],
    ".": [],
    "S": [(1, 0), (-1, 0), (0, 1), (0, -1)]
}


def next_motion(prev_motion, pipe):
    conns = connections[pipe]
    for conn in conns:
        if inv(prev_motion) != conn:
            return conn
    return None


def inv(motion):
    return -motion[0], -motion[1]


def connected(a, b, motion):
    return motion in connections[a] and inv(motion) in connections[b]


def part1(fname="day10_input.txt"):
    s_loc = None
    with open(fname, "r") as f:
        lines = f.readlines()
        for x, line in enumerate(lines):
            for y, char in enumerate(line[:-1]):
                if char == "S":
                    s_loc = (x, y)
                    break

    for start_motion in connections["S"]:
        count = 0
        cur_x = s_loc[0]
        cur_y = s_loc[1]
        next_x = s_loc[0] + start_motion[0]
        next_y = s_loc[1] + start_motion[1]
        motion = start_motion

        while next_x != s_loc[0] or next_y != s_loc[1]:
            count += 1
            if connected(lines[cur_x][cur_y], lines[next_x][next_y], motion):
                cur_x = next_x
                cur_y = next_y

                motion = next_motion(motion, lines[cur_x][cur_y])

                next_x = cur_x + motion[0]
                next_y = cur_y + motion[1]

                if motion is None:
                    break
            else:
                break
        else:
            return count // 2 + 1


def part2(fname="day10_input.txt"):
    s_loc = None
    with open(fname, "r") as f:
        lines = f.readlines()
        x_max = len(lines)
        y_max = len(lines[0]) - 1
        for x, line in enumerate(lines):
            for y, char in enumerate(line[:-1]):
                if char == "S":
                    s_loc = (x, y)
                    break

    for start_motion in connections["S"]:
        part_map = {}
        count = 0
        cur_x = s_loc[0]
        cur_y = s_loc[1]
        next_x = s_loc[0] + start_motion[0]
        next_y = s_loc[1] + start_motion[1]
        motion = start_motion

        while next_x != s_loc[0] or next_y != s_loc[1]:
            count += 1
            if connected(lines[cur_x][cur_y], lines[next_x][next_y], motion):
                part_map[(next_x, next_y)] = lines[next_x][next_y]
                cur_x = next_x
                cur_y = next_y

                motion = next_motion(motion, lines[cur_x][cur_y])

                next_x = cur_x + motion[0]
                next_y = cur_y + motion[1]

                if motion is None:
                    break
            else:
                break
        else:
            # figure out what shape the S is
            for conn in ["L", "F", "J", "7", "|", "-"]:
                if start_motion in connections[conn] and inv(motion) in connections[conn]:
                    s_part = conn
                    break
            else:
                assert False
            part_map[(next_x, next_y)] = s_part
            break

    # count inner spaces
    count = 0
    last_turn = None
    for x in range(x_max):
        inside = False
        for y in range(y_max):
            if (x, y) in part_map:
                if part_map[x, y] == "|":
                    inside = not inside
                if part_map[x, y] == "J":
                    if last_turn == "F":
                        inside = not inside
                    last_turn = None
                if part_map[x, y] == "7":
                    if last_turn == "L":
                        inside = not inside
                    last_turn = None
                if part_map[x, y] == "F":
                    last_turn = "F"
                if part_map[x, y] == "L":
                    last_turn = "L"
            else:
                if inside:
                    count += 1
    return count


print(part1(fname="day10_test.txt"))
print(part1(fname="day10_input.txt"))
print(part2(fname="day10_test.txt"))
print(part2(fname="day10_test2.txt"))
print(part2(fname="day10_test3.txt"))
print(part2(fname="day10_input.txt"))
