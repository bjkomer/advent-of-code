import numpy as np


# Parsing File
with open("day4_input.txt", "r") as f:
    lines = f.readlines()
    n_boards = (len(lines)-1)//6 # divide by 6 because of the blank lines
    draw = lines[0][:-1].split(",")

    boards = np.zeros((n_boards, 5, 5), dtype=np.int32)

    for i in range(n_boards):
        for j in range(5):
            for k in range(5):
                boards[i, j, k] = int(lines[i*6+2+j][(k*3):((k+1)*3)])

# for checking if a row/column is complete
win = np.ones((5,)) * -1

# Part 1
def part1():
    for num in draw:
        indices = np.where(boards==int(num))
        boards[indices] = -1

        # check all changed numbers to see if any board wins
        for b, x, y in zip(*indices):
            if np.allclose(boards[b, x, :], win) or np.allclose(boards[b, :, y], win):
                score = np.sum(np.clip(boards[b, :, :], 0, 100)) * int(num)
                return score

# Part 2
def part2():
    boards_left = np.ones((n_boards,))
    for num in draw:
        indices = np.where(boards==int(num))
        boards[indices] = -1

        # check all changed numbers to see if any board wins
        for b, x, y in zip(*indices):
            if np.allclose(boards[b, x, :], win) or np.allclose(boards[b, :, y], win):
                if boards_left[b] and np.sum(boards_left) == 1:  # this is the final board
                    score = np.sum(np.clip(boards[b, :, :], 0, 100)) * int(num)
                    return score
                else:
                    boards_left[b] = 0

print(part1())
print(part2())
