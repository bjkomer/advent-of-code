import numpy as np

def get_data():
    with open("day13_input.txt", "r") as f:
        lines = f.readlines()
        folding = False
        coords = []
        folds = []
        max_x = 0
        max_y = 0
        for line in lines:
            if line == "\n": # switch to building folds after the newline
                folding = True
            elif folding:
                # tuple of x or y, and then the position
                folds.append((line[11], int(line[13:-1])))
            else:
                x, y = line[:-1].split(",")
                coords.append([int(x), int(y)])
                max_x = max(max_x, coords[-1][0])
                max_y = max(max_y, coords[-1][1])
    return coords, folds, max_x, max_y

def fold_line(coords, ind, loc, max_x, max_y):
    for i in range(len(coords)):
        if coords[i][ind] > loc:
            diff = coords[i][ind] - loc
            coords[i][ind] -= diff * 2
    return coords

    
def part1():
    coords, folds, max_x, max_y = get_data()

    if folds[0][0] == "x":
        ind = 0
    else:
        ind = 1

    loc = folds[0][1]

    fold_line(coords, ind, loc, max_x, max_y)

    points = {}
    for coord in coords:
        points[tuple(coord)] = 1
    return len(points.keys())


def part2():
    coords, folds, max_x, max_y = get_data()

    for fold in folds:
        if fold[0] == "x":
            ind = 0
        else:
            ind = 1

        loc = fold[1]

        fold_line(coords, ind, loc, max_x, max_y)

        if ind == 0:
            max_x = loc
        else:
            max_y = loc

    arr = np.zeros((max_x, max_y))

    for coord in coords:
        arr[coord[0], coord[1]] = 1

    # Generate readable output
    out_str = ""
    for j in range(max_y):
        for i in range(max_x):
            if arr[i, j] == 1:
                out_str += "#"
            else:
                out_str += " "
        out_str += "\n"

    return out_str

print(part1())
print(part2())

