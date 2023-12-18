def part1(fname="day2_input.txt"):
    total = 0
    with open(fname, "r") as f:
        lines = f.readlines()
        for line in lines:
            line = line[:-1]
            game_txt, cube_txt = line.split(": ")
            id_num = int(game_txt.split(" ")[1])
            trials = cube_txt.split("; ")
            c = {"red":0, "green": 0, "blue": 0}
            for trial in trials:
                checks = trial.split(", ")
                for check in checks:
                    num, colour = check.split(" ")
                    num = int(num)
                    c[colour] = max(c[colour], num)
            if c["red"] > 12 or c["green"] > 13 or c["blue"] > 14:
                pass
            else:
                total += id_num

    return total

def part2(fname="day2_input.txt"):
    total = 0
    with open(fname, "r") as f:
        lines = f.readlines()
        for line in lines:
            line = line[:-1]
            game_txt, cube_txt = line.split(": ")
            id_num = int(game_txt.split(" ")[1])
            trials = cube_txt.split("; ")
            c = {"red":0, "green": 0, "blue": 0}
            for trial in trials:
                checks = trial.split(", ")
                for check in checks:
                    num, colour = check.split(" ")
                    num = int(num)
                    c[colour] = max(c[colour], num)
            total += c["red"] * c["green"] * c["blue"]

    return total


print(part1("day2_test.txt"))
print(part1("day2_input.txt"))
print(part2("day2_test.txt"))
print(part2("day2_input.txt"))

