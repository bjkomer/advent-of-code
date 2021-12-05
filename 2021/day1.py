import numpy as np


with open("day1_input.txt", "r") as f:
    data = np.array([int(x) for x in f.readlines()])

# Part 1
count = 0
for i in range(1, len(data)):
    if data[i] > data[i-1]:
        count += 1

print(count)

# Part 2
count = 0
current_sum = np.sum(data[:3])
for i in range(3, len(data)):
    new_sum = current_sum - data[i-3] + data[i]
    if new_sum > current_sum:
        count +=1
    current_sum = new_sum

print(count)

