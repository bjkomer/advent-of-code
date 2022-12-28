import numpy as np


class Monkey(object):

    def __init__(self, items, operation, test, divide_worry=False):
        self.items = items
        self.operation = operation
        self.test = test
        self.inspections = 0
        self.divide_worry = divide_worry

    def turn(self):

        throws = []

        for item in self.items:
            new_worry = self.operation(item)
            if self.divide_worry:
                new_worry = new_worry // 3
            else:
                new_worry = new_worry % (5 * 17 * 2 * 7 * 3 * 11 * 13 * 19)
            target = self.test(new_worry)
            throws.append((target, new_worry))
            self.inspections += 1
        # All items will be thrown, so monkey will have no items left
        self.items = []

        return throws


def parse_input(fname="day11_input.txt"):
    # Note: skipping parser for speed
    # with open(fname, "r") as f:
 #        lines = f.readlines()
    monkeys = []

    # Monkey 0
    monkeys.append(
        Monkey(
            items=[77, 69, 76, 77, 50, 58],
            operation=lambda x: x * 11,
            test=lambda x: 1 if x % 5 == 0 else 5,
        )
    )

    # Monkey 1
    monkeys.append(
        Monkey(
            items=[75, 70, 82, 83, 96, 64, 62],
            operation=lambda x: x + 8,
            test=lambda x: 5 if x % 17 == 0 else 6,
        )
    )

    # Monkey 2
    monkeys.append(
        Monkey(
            items=[53],
            operation=lambda x: x * 3,
            test=lambda x: 0 if x % 2 == 0 else 7,
        )
    )

    # Monkey 3
    monkeys.append(
        Monkey(
            items=[85, 64, 93, 64, 99],
            operation=lambda x: x + 4,
            test=lambda x: 7 if x % 7 == 0 else 2,
        )
    )

    # Monkey 4
    monkeys.append(
        Monkey(
            items=[61, 92, 71],
            operation=lambda x: x * x,
            test=lambda x: 2 if x % 3 == 0 else 3,
        )
    )

    # Monkey 5
    monkeys.append(
        Monkey(
            items=[79, 73, 50, 90],
            operation=lambda x: x + 2,
            test=lambda x: 4 if x % 11 == 0 else 6,
        )
    )

    # Monkey 6
    monkeys.append(
        Monkey(
            items=[50, 89],
            operation=lambda x: x + 3,
            test=lambda x: 4 if x % 13 == 0 else 3,
        )
    )

    # Monkey 7
    monkeys.append(
        Monkey(
            items=[83, 56, 64, 58, 93, 91, 56, 65],
            operation=lambda x: x + 5,
            test=lambda x: 1 if x % 19 == 0 else 0,
        )
    )

    return monkeys

def part1(fname="day11_input.txt"):
    monkeys = parse_input(fname=fname)

    for _ in range(20):
        for monkey in monkeys:
            throws = monkey.turn()
            for throw in throws:
                monkeys[throw[0]].items.append(throw[1])

    inspections = sorted([monkey.inspections for monkey in monkeys])
    print(inspections)
    return inspections[-1] * inspections[-2]

def part2(fname="day11_input.txt", n_rounds=10000):
    monkeys = parse_input(fname=fname)

    inspections = np.zeros((n_rounds, len(monkeys)))

    for r in range(n_rounds):
        for i, monkey in enumerate(monkeys):
            throws = monkey.turn()
            for throw in throws:
                monkeys[throw[0]].items.append(throw[1])
            inspections[r, i] = monkeys[i].inspections

    inspections = sorted([monkey.inspections for monkey in monkeys])
    print(inspections)
    return inspections[-1] * inspections[-2]


print(part1())
print(part2(n_rounds=10000))
