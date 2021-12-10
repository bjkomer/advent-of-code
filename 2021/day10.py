def part1():
    points = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }
    match = {
        '(':')',
        '[':']',
        '{':'}',
        '<':'>',
    }
    score = 0
    with open("day10_input.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            stack = []
            for char in line[:-1]:  # trim off the newline
                # left paren is always valid
                if char in '([{<':
                    stack.append(char)
                elif len(stack) == 0:  # cannot open with a closing paren
                    score += points[char]
                    break
                elif match[stack[-1]] == char:  # correct match, remove them
                    stack.pop()
                else:
                    score += points[char]
                    break

    return score


def part2():
    points = {
        '(': 1,
        '[': 2,
        '{': 3,
        '<': 4,
    }
    match = {
        '(':')',
        '[':']',
        '{':'}',
        '<':'>',
    }
    scores = []
    with open("day10_input.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            stack = []
            for char in line[:-1]:  # trim off the newline
                # left paren is always valid
                if char in '([{<':
                    stack.append(char)
                elif len(stack) == 0:  # cannot open with a closing paren
                    break
                elif match[stack[-1]] == char:  # correct match, remove them
                    stack.pop()
                else:
                    break
            else:  # only gets here if there is no corruption
                # stack will contain only opening parenthesis at this point
                # go backwards to tally the score
                score = 0
                for p in stack[::-1]:
                    score = score * 5 + points[p]
                scores.append(score)

    # return the middle score
    return sorted(scores)[len(scores)//2]

print(part1())
print(part2())

