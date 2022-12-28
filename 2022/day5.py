def parse_command(line):
    num, rest = line[5:].split(" from ")
    start_ind, end_ind = rest.split(" to ")
    return (int(num), int(start_ind) - 1, int(end_ind) - 1)

def parse_input(fname="day5_input.txt"):
    commands = []
    stacks = []

    with open(fname, "r") as f:
        lines = f.readlines()
        stack_lines = []
        i = 0
        while len(lines[i]) > 3:
            stack_lines.append(lines[i])
            i+=1

        # each stack takes up four characters, rounding down due to newlines at the end
        n_stacks = len(stack_lines[-1]) // 4

        # Initialize empty list for each stack
        stacks = [[] for j in range(n_stacks)]
        # The last line added is just the labels, so it should be ignored
        for j in range(i-2, -1, -1):
            for k in range(n_stacks):
                char = stack_lines[j][k*4 + 1]
                if char != " ":
                    stacks[k].append(char)
        
        for j in range(i + 1, len(lines)):
            commands.append(parse_command(lines[j]))

    return stacks, commands

def part1(fname="day5_input.txt"):
    stacks, commands = parse_input(fname=fname)

    for command in commands:
        for i in range(command[0]):
            stacks[command[2]].append(stacks[command[1]].pop())

    ret = ""
    for stack in stacks:
        ret += stack[-1]
    return ret

def part2(fname="day5_input.txt"):
    stacks, commands = parse_input(fname=fname)

    for command in commands:
        tmp = []
        for i in range(command[0]):
            tmp.append(stacks[command[1]].pop())
        for i in range(command[0]-1, -1, -1):
            stacks[command[2]].append(tmp[i])

    ret = ""
    for stack in stacks:
        ret += stack[-1]
    return ret


print(part1())
print(part2())
