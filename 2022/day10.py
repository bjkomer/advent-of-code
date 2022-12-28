import numpy as np

def parse_input(fname="day10_input.txt"):
    # Series of tuples of (cycles, modification)
    commands = []
    with open(fname, "r") as f:
        lines = f.readlines()
        for line in lines:
            if line.strip() == "noop":
                commands.append((1, 0))
            else:
                commands.append((2, int(line.strip().split(" ")[1])))
    return commands

def part1(fname="day10_input.txt"):
    commands = parse_input(fname=fname)
    signal_strength = 0
    cycle = 1
    value = 1
    key_cycles = [220, 180, 140, 100, 60, 20]
    for command in commands:
        cycle += command[0]
        value += command[1]
        if cycle >= key_cycles[-1]:
            signal_strength += key_cycles[-1] * value
            key_cycles.pop()
            if len(key_cycles) == 0:
                break
        
    return signal_strength


def render(screen):
    screen_string = ""
    for i in range(6):
        for j in range(40):
            if screen[i*40+j] == 1:
                screen_string += "#"
            else:
                screen_string += "."
        screen_string += "\n"
    return screen_string


def part2(fname="day10_input.txt"):
    commands = parse_input(fname=fname)
    cycle = 0
    value = 1
    screen = np.zeros((40*6))

    for command in commands:
        for i in range(command[0]):
            if abs(value - cycle % 40) < 2:
                screen[cycle] = 1
            cycle += 1
        else:
            value += command[1]
        



    return render(screen)


print(part1())
print(part2())
