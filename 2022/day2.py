
def part1():
    score = 0
    with open("day2_input.txt") as f:
        lines = f.readlines()
        for line in lines:
            if line[2] == "X":  # Rock
                score += 1
                if line[0] == "A":  # Rock
                    score += 3
                elif line[0] == "C":  # Scissors
                    score += 6
            elif line[2] == "Y":  # Paper
                score += 2
                if line[0] == "A":  # Rock
                    score += 6
                elif line[0] == "B":  # Paper
                    score += 3
            elif line[2] == "Z":  # Scissors
                score += 3
                if line[0] == "B":  # Paper
                    score += 6
                elif line[0] == "C":  # Scissors
                    score += 3
    return score

def part2():
    score = 0
    with open("day2_input.txt") as f:
        lines = f.readlines()
        for line in lines:
            if line[0] == "A":  # Rock
                if line[2] == "X":  # Lose
                    score += 0 + 3
                elif line[2] == "Y":  # Draw
                    score += 3 + 1
                elif line[2] == "Z":  # Win
                    score += 6 + 2
            elif line[0] == "B":  # Paper
                if line[2] == "X":  # Lose
                    score += 0 + 1
                elif line[2] == "Y":  # Draw
                    score += 3 + 2
                elif line[2] == "Z":  # Win
                    score += 6 + 3
            elif line[0] == "C":  # Scissors
                if line[2] == "X":  # Lose
                    score += 0 + 2
                elif line[2] == "Y":  # Draw
                    score += 3 + 3
                elif line[2] == "Z":  # Win
                    score += 6 + 1
    return score

print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
