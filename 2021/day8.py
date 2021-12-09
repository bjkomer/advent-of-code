def part1():
    count = 0
    with open("day8_input.txt", "r") as f:
        for line in f.readlines():
            first, second = line[:-1].split("|")
            outputs = second.strip().split(" ")

            for digit in outputs:
                if len(digit) == 2 or len(digit) == 3 or len(digit) == 4 or len(digit) == 7:
                    count += 1
    return count


def within(a, b):
    for char in a:
        if not (char in b):
            return False
    return True


def decode_digits(inputs, outputs):
    # 5-segment: 2, 3, 5
    # 6-segment: 0, 6, 9
    # can determine 'a' with 100% certainty using 1 and 7, but we don't actually need to know any connections
    # can determine which 5-segment number is 3 because it will overlap fully with 1
    # can determine which 6-segment number is 9 because it will overlap fully with 4
    # can determine which 6-segment number is 0 because it will overlap fully with 7 and not be 9
    # can determine which 6-segment number is 6 because it is not 0 or 9
    # can determine which 5-segment number is 5 because it can fit within 6 or 9
    # can determine which 5-segment number is 2 because it is the only one left

    # remove all order information
    input_set = ["".join(sorted(x)) for x in inputs]
    output_set = ["".join(sorted(x)) for x in outputs]


    # mappings between digits and segments
    dig_to_seg = {}
    seg_to_dig = {}

    def check(digit, seg):
        if digit == 3:
            return len(seg) == 5 and within(dig_to_seg[1], seg)
        if digit == 9:
            return len(seg) == 6 and within(dig_to_seg[4], seg)
        if digit == 0:
            return len(seg) == 6 and within(dig_to_seg[7], seg) and seg != dig_to_seg[9]
        if digit == 6:
            return len(seg) == 6 and seg != dig_to_seg[0] and seg != dig_to_seg[9]
        if digit == 5:
            return len(seg) == 5 and seg != dig_to_seg[3] and within(seg, dig_to_seg[9])
        if digit == 2:
            return len(seg) == 5 and seg != dig_to_seg[5] and seg != dig_to_seg[3]


    # TODO: can make things slightly faster by removing solved digits from input_set
    # Fill in the values known initially
    for seg in input_set:
        if len(seg) == 2:  # digit is 1
            dig_to_seg[1] = seg
            seg_to_dig[seg] = 1
        elif len(seg) == 3:  # digit is 7
            dig_to_seg[7] = seg
            seg_to_dig[seg] = 7
        elif len(seg) == 4:  # digit is 4
            dig_to_seg[4] = seg
            seg_to_dig[seg] = 4
        elif len(seg) == 7:  # digit is 8
            dig_to_seg[8] = seg
            seg_to_dig[seg] = 8


    # Note: Solve function assumes this order of digits
    for digit in [3, 9, 0, 6, 5, 2]:
        for seg in input_set:
            if check(digit, seg):
                dig_to_seg[digit] = seg
                seg_to_dig[seg] = digit
                break
        else:
            raise RuntimeError(f"Digit {digit} could not be determined")


    # Compute output value
    value = ""
    for seg in output_set:
        value += str(seg_to_dig[seg])

    return int(value)


def part2():
    count = 0
    with open("day8_input.txt", "r") as f:
        for line in f.readlines():
            first, second = line[:-1].split("|")
            inputs = first.strip().split(" ")
            outputs = second.strip().split(" ")

            count += decode_digits(inputs, outputs)

    return count


print(part1())
print(part2())

