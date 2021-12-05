import numpy as np


# Part 1
with open("day3_input.txt", "r") as f:
    raw_data = f.readlines()
    n_lines = len(raw_data)
    n_bits = len(raw_data[0]) - 1
    array = np.zeros((n_bits,))
    for line in raw_data:
        for i, char in enumerate(line.strip()):
            if char == '0' or char == '1':
                array[i] += int(char)

array /= n_lines
bits = array > 0.5

gamma = ''
epsilon = ''

for bit in bits:
    if bit:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

print(int(gamma, 2) * int(epsilon, 2))

# Part 2
with open("day3_input.txt", "r") as f:
    raw_data = f.readlines()
    n_lines = len(raw_data)
    n_bits = len(raw_data[0]) - 1
    array = np.zeros((n_lines, n_bits,))
    for i, line in enumerate(raw_data):
        for j, char in enumerate(line.strip()):
            if char == '0' or char == '1':
                array[i, j] = int(char)

# now work with the arrays to find both numbers
gamma = ''
epsilon = ''

gamma_inds = np.ones((n_lines,))
epsilon_inds = np.ones((n_lines,))

for i in range(n_bits):
    # gamma
    if np.sum(gamma_inds) > 0:
        keep_bit = (np.sum(array[np.where(gamma_inds==1), i]) / np.sum(gamma_inds)) >= .5
        gamma += str(int(keep_bit))
        # remove the ones that don't match
        top_val_gamma = array[np.where(gamma_inds==1)][0, :]
        gamma_inds[np.where(array[:, i] != keep_bit)] = 0
        if np.sum(gamma_inds) == 0:
            gamma = ''
            for n in top_val_gamma:
                gamma += str(int(n))


    # epsilon
    if np.sum(epsilon_inds) > 0:
        keep_bit = (np.sum(array[np.where(epsilon_inds==1), i]) / np.sum(epsilon_inds)) < .5
        epsilon += str(int(keep_bit))
        # remove the ones that don't match
        top_val_epsilon = array[np.where(epsilon_inds==1)][0, :]
        epsilon_inds[np.where(array[:, i] != keep_bit)] = 0
        if np.sum(epsilon_inds) == 0:
            epsilon = ''
            for n in top_val_epsilon:
                epsilon += str(int(n))

print(int(gamma, 2) * int(epsilon, 2))
