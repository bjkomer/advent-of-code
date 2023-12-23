class Brick:

    def __init__(self, lower, upper):
        self.lower = lower
        self.upper = upper

    def __repr__(self):
        return f"({self.lower}, {self.upper})"


def intersect(b1, b2):

    return (
                   (b1.lower[0] <= b2.lower[0] <= b1.upper[0]) or
                   (b1.lower[0] <= b2.upper[0] <= b1.upper[0]) or
                   (b2.lower[0] <= b1.lower[0] <= b2.upper[0]) or
                   (b2.lower[0] <= b1.upper[0] <= b2.upper[0])
           ) and \
           (
                   (b1.lower[1] <= b2.lower[1] <= b1.upper[1]) or
                   (b1.lower[1] <= b2.upper[1] <= b1.upper[1]) or
                   (b2.lower[1] <= b1.lower[1] <= b2.upper[1]) or
                   (b2.lower[1] <= b1.upper[1] <= b2.upper[1])
           ) and \
           (
                   (b1.lower[2] <= b2.lower[2] <= b1.upper[2]) or
                   (b1.lower[2] <= b2.upper[2] <= b1.upper[2]) or
                   (b2.lower[2] <= b1.lower[2] <= b2.upper[2]) or
                   (b2.lower[2] <= b1.upper[2] <= b2.upper[2])
           )


def part1(fname="day22_input.txt"):
    bricks = {}
    with open(fname, "r") as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            start, end = line[:-1].split("~")
            brick = (
                tuple([int(c) for c in start.split(",")]),
                tuple([int(c) for c in end.split(",")]),
            )
            bricks[i] = Brick(lower=brick[0], upper=brick[1])

    # make bricks fall, starting with lowest bricks
    brick_list = sorted(list(bricks.values()), key=lambda x: x.lower[2])

    for brick in brick_list:
        if brick.lower[2] > 1:
            virtual_brick = Brick(
                (brick.lower[0], brick.lower[1], 1),
                (brick.upper[0], brick.upper[1], brick.lower[2] - 1)
            )
            intersections = [int_brick for int_brick in brick_list if intersect(virtual_brick, int_brick)]
            highest_intersection = max([0] + [b.upper[2] for b in intersections])

            drop = brick.lower[2] - highest_intersection - 1
            if drop > 0:
                brick.lower = (brick.lower[0], brick.lower[1], brick.lower[2] - drop)
                brick.upper = (brick.upper[0], brick.upper[1], brick.upper[2] - drop)

    count = 0
    for id, brick in bricks.items():
        virtual_brick = Brick(
            (brick.lower[0], brick.lower[1], brick.upper[2] + 1),
            (brick.upper[0], brick.upper[1], brick.upper[2] + 1)
        )
        intersections = [int_brick for int_brick in brick_list if intersect(virtual_brick, int_brick)]
        if len(intersections) == 0:
            # supporting no bricks, can remove
            count += 1
        else:
            for supported_brick in intersections:
                virtual_support = Brick(
                    (supported_brick.lower[0], supported_brick.lower[1], supported_brick.lower[2] - 1),
                    (supported_brick.upper[0], supported_brick.upper[1], supported_brick.lower[2] - 1)
                )
                supported_intersections = [int_brick for int_brick in brick_list if intersect(virtual_support, int_brick)]
                if len(supported_intersections) == 1:
                    # The current brick is the only support
                    break
            else:
                count += 1

    return count


def part2(fname="day22_input.txt"):
    bricks = {}
    with open(fname, "r") as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            start, end = line[:-1].split("~")
            brick = (
                tuple([int(c) for c in start.split(",")]),
                tuple([int(c) for c in end.split(",")]),
            )
            bricks[i] = Brick(lower=brick[0], upper=brick[1])

    # make bricks fall, starting with lowest bricks
    brick_list = sorted(list(bricks.values()), key=lambda x: x.lower[2])

    for brick in brick_list:
        if brick.lower[2] > 1:
            virtual_brick = Brick(
                (brick.lower[0], brick.lower[1], 1),
                (brick.upper[0], brick.upper[1], brick.lower[2] - 1)
            )
            intersections = [int_brick for int_brick in brick_list if intersect(virtual_brick, int_brick)]
            highest_intersection = max([0] + [b.upper[2] for b in intersections])

            drop = brick.lower[2] - highest_intersection - 1
            if drop > 0:
                brick.lower = (brick.lower[0], brick.lower[1], brick.lower[2] - drop)
                brick.upper = (brick.upper[0], brick.upper[1], brick.upper[2] - drop)

    total_fall = 0
    brick_list = sorted(list(bricks.values()), key=lambda x: x.lower[2])
    # delete every brick, and count the number of falls
    for removed_brick in brick_list:
        leftover_bricks = [Brick(b.lower, b.upper) for b in brick_list if b != removed_brick]
        for brick in leftover_bricks:
            if brick.lower[2] > 1:
                virtual_brick = Brick(
                    (brick.lower[0], brick.lower[1], 1),
                    (brick.upper[0], brick.upper[1], brick.lower[2] - 1)
                )
                intersections = [int_brick for int_brick in leftover_bricks if intersect(virtual_brick, int_brick)]
                highest_intersection = max([0] + [b.upper[2] for b in intersections])

                drop = brick.lower[2] - highest_intersection - 1
                if drop > 0:
                    total_fall += 1
                    brick.lower = (brick.lower[0], brick.lower[1], brick.lower[2] - drop)
                    brick.upper = (brick.upper[0], brick.upper[1], brick.upper[2] - drop)

    return total_fall


print(part1(fname="day22_test.txt"))
print(part1(fname="day22_input.txt"))
print(part2(fname="day22_test.txt"))
print(part2(fname="day22_input.txt"))
