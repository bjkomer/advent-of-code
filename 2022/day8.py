import numpy as np
import matplotlib.pyplot as plt


def parse_input(fname="day8_input.txt"):
    with open(fname, "r") as f:
        lines = f.readlines()
        rows = len(lines)
        columns = len(lines[0].strip())

        trees = np.zeros((rows, columns))

        for r, line in enumerate(lines):
            for c, char in enumerate(line.strip()):
                trees[r, c] = int(char)
    return trees

def part1(fname="day8_input.txt"):
    trees = parse_input(fname=fname)
    visible = np.zeros_like(trees)

    # All of the edges are visible
    visible[0, :] = 1
    visible[-1, :] = 1
    visible[:, 0] = 1
    visible[:, -1] = 1

    for i in range(1, trees.shape[0] - 1):
        # Top to bottom
        height = trees[i, 0]
        for j in range(1, trees.shape[1] - 1):
            if trees[i, j] > height:
                visible[i, j] = 1
                height = max(height, trees[i, j])
            elif height == 9:  # As soon as one tree is too tall, break the loop
                break

        # Bottom to top
        height = trees[i, -1]
        for j in range(trees.shape[1] - 2, 0, -1):
            if trees[i, j] > height:
                visible[i, j] = 1
                height = max(height, trees[i, j])
            elif height == 9:  # As soon as one tree is too tall, break the loop
                break

    for j in range(1, trees.shape[1] - 1):
        # Top to bottom
        height = trees[0, j]
        for i in range(1, trees.shape[0] - 1):
            if trees[i, j] > height:
                visible[i, j] = 1
                height = max(height, trees[i, j])
            elif height == 9:  # As soon as one tree is too tall, break the loop
                break

        # Bottom to top
        height = trees[-1, j]
        for i in range(trees.shape[0] - 2, 0, -1):
            if trees[i, j] > height:
                visible[i, j] = 1
                height = max(height, trees[i, j])
            elif height == 9:  # As soon as one tree is too tall, break the loop
                break

    # plt.imshow(trees)
    # plt.imshow(visible)
    # plt.show()

    return np.sum(visible)

def part2(fname="day8_input.txt"):
    trees = parse_input(fname=fname)
    # Brute force method
    best_score = 0
    # The very edges will have a scenic score of 0, so ignore them
    for i in range(1, trees.shape[0] - 1):
        for j in range(1, trees.shape[1] - 1):
            height = trees[i, j]
            views = []
            for count, ii in enumerate(range(i + 1, trees.shape[0])):
                if trees[ii, j] >= height:
                    break
            views.append(count + 1)

            for count, ii in enumerate(range(i - 1, -1, -1)):
                if trees[ii, j] >= height:
                    break
            views.append(count + 1)

            for count, jj in enumerate(range(j + 1, trees.shape[1])):
                if trees[i, jj] >= height:
                    break
            views.append(count + 1)

            for count, jj in enumerate(range(j - 1, -1, -1)):
                if trees[i, jj] >= height:
                    break
            views.append(count + 1)

            best_score = max(best_score, views[0]*views[1]*views[2]*views[3])
    return best_score




print(part1())
print(part2())
