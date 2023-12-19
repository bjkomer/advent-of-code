def accepted(part, proc, processes):
    if proc == "R":
        return False
    elif proc == "A":
        return True
    else:
        for check in processes[proc][:-1]:
            k = check[0]  # key
            c = check[1]  # comparator
            v = check[2]  # value
            o = check[3]  # output name
            if c == ">" and part[k] > v:
                return accepted(part, o, processes)
            elif c == "<" and part[k] < v:
                return accepted(part, o, processes)
        else:
            return accepted(part, processes[proc][-1], processes)


def part1(fname="day19_input.txt"):
    with open(fname, "r") as f:
        lines = f.readlines()
        read_parts = False
        processes = {}
        parts = []
        for line in lines:
            if line == "\n":
                read_parts = True
                continue
            if read_parts:
                values = line[1:-2].split(",")
                part = {}
                for value in values:
                    k, v = value.split("=")
                    part[k] = int(v)
                parts.append(part)
            else:
                name, rest = line[:-1].split("{")
                commands = rest[:-1].split(",")
                processes[name] = []
                for i, command in enumerate(commands):
                    if i == len(commands) - 1:
                        processes[name].append(command)
                    else:
                        check_key = command[0]
                        comparator = command[1]
                        value, output = command[2:].split(":")
                        processes[name].append((check_key, comparator, int(value), output))

    total = 0

    for part in parts:
        if accepted(part, "in", processes):
            total += (part["x"] + part["m"] + part["a"] + part["s"])

    return total


def split_part(part, rules):
    new_parts = []
    remaining = part.copy()
    for check in rules[:-1]:
        k = check[0]  # key
        c = check[1]  # comparator
        v = check[2]  # value
        o = check[3]  # output name
        if c == ">":
            min_val = remaining[f"min_{k}"]
            max_val = remaining[f"max_{k}"]
            if max_val > v:  # at least partial match
                if min_val > v:
                    # full match, no remaining
                    matched_part = remaining.copy()
                    matched_part["rule"] = o
                    return new_parts + [matched_part]
                else:
                    matched_part = remaining.copy()
                    matched_part["rule"] = o
                    matched_part[f"min_{k}"] = v + 1
                    new_parts.append(matched_part)

                    remaining[f"max_{k}"] = v
        if c == "<":
            min_val = remaining[f"min_{k}"]
            max_val = remaining[f"max_{k}"]
            if min_val < v:  # at least partial match
                if max_val < v:
                    # full match, no remaining
                    matched_part = remaining.copy()
                    matched_part["rule"] = o
                    return new_parts + [matched_part]
                else:
                    matched_part = remaining.copy()
                    matched_part["rule"] = o
                    matched_part[f"max_{k}"] = v - 1
                    new_parts.append(matched_part)

                    remaining[f"min_{k}"] = v
    else:
        remaining["rule"] = rules[-1]
        return new_parts + [remaining]


def part2(fname="day19_input.txt"):
    with open(fname, "r") as f:
        lines = f.readlines()
        processes = {}
        for line in lines:
            if line == "\n":
                break
            name, rest = line[:-1].split("{")
            commands = rest[:-1].split(",")
            processes[name] = []
            for i, command in enumerate(commands):
                if i == len(commands) - 1:
                    processes[name].append(command)
                else:
                    check_key = command[0]
                    comparator = command[1]
                    value, output = command[2:].split(":")
                    processes[name].append((check_key, comparator, int(value), output))

        initial_part = {
            "min_x": 1,
            "max_x": 4000,
            "min_m": 1,
            "max_m": 4000,
            "min_a": 1,
            "max_a": 4000,
            "min_s": 1,
            "max_s": 4000,
            "rule": "in",
        }

        parts_left = [initial_part]

        accepted_parts = []

        while len(parts_left) > 0:
            cur_part = parts_left.pop()
            new_parts = split_part(cur_part, processes[cur_part["rule"]])
            for part in new_parts:
                if part["rule"] == "A":
                    accepted_parts.append(part)
                elif part["rule"] != "R":
                    parts_left.append(part)

        # count possibilities
        total = 0
        for part in accepted_parts:
            total += (part["max_x"] - part["min_x"] + 1) *\
                     (part["max_m"] - part["min_m"] + 1) *\
                     (part["max_a"] - part["min_a"] + 1) *\
                     (part["max_s"] - part["min_s"] + 1)

        return total


print(part1(fname="day19_test.txt"))
print(part1(fname="day19_input.txt"))
print(part2(fname="day19_test.txt"))
print(part2(fname="day19_input.txt"))
