from collections import defaultdict


class FlipFlop:
    def __init__(self, name, connections):
        self.name = name
        self.on = False
        self.connections = connections

    def initialize(self):
        pass

    def receive_pulse(self, inp, pulse):
        if not pulse:
            self.on = not self.on
            return [(c, self.name, self.on) for c in self.connections]
        return []


class Conjunction:
    def __init__(self, name, connections):
        self.name = name
        self.inputs = []
        self.connections = connections

    def initialize(self):
        self.prev_pulses = {i:False for i in self.inputs}
        self.debug = []

    def receive_pulse(self, inp, pulse):
        self.prev_pulses[inp] = pulse
        if self.name == "qn":
            if pulse:
                self.debug.append(inp)
        if all([p for p in self.prev_pulses.values()]):
            return [(c, self.name, False) for c in self.connections]
        else:
            return [(c, self.name, True) for c in self.connections]



def part1(fname="day20_input.txt"):
    components = {}
    broadcaster = None
    flipflops = {}
    conjunctions = {}
    with open(fname, "r") as f:
        lines = f.readlines()
        for line in lines:
            block, outputs = line[:-1].split(" -> ")
            if block == "broadcaster":
                broadcaster = outputs.split(", ")
            elif block[0] == "%":
                flipflops[block[1:]] = outputs.split(", ")
                components[block[1:]] = FlipFlop(block[1:], outputs.split(", "))
            elif block[0] == "&":
                conjunctions[block[1:]] = outputs.split(", ")
                components[block[1:]] = Conjunction(block[1:], outputs.split(", "))
    for name, outputs in components.items():
        for output in outputs.connections:
            if output in conjunctions:
                components[output].inputs.append(name)
    for output in broadcaster:
        if output in conjunctions:
            components[output].inputs.append("broadcaster")

    for name, comp in components.items():
        comp.initialize()

    low_count = 0
    high_count = 0
    for _ in range(1000):
        low_count += 1  # initial button
        pulses = [(c, "broadcaster", False) for c in broadcaster]
        while len(pulses) > 0:
            low_count += len([p for p in pulses if not p[2]])
            high_count += len([p for p in pulses if p[2]])
            new_pulses = []
            for pulse in pulses:
                if pulse[0] in components:
                    new_pulses.extend(components[pulse[0]].receive_pulse(pulse[1], pulse[2]))

            pulses = new_pulses

    print(f"{low_count=}")
    print(f"{high_count=}")
    return low_count * high_count


def part2(fname="day20_input.txt"):
    components = {}
    broadcaster = None
    flipflops = {}
    conjunctions = {}
    with open(fname, "r") as f:
        lines = f.readlines()
        for line in lines:
            block, outputs = line[:-1].split(" -> ")
            if block == "broadcaster":
                broadcaster = outputs.split(", ")
            elif block[0] == "%":
                flipflops[block[1:]] = outputs.split(", ")
                components[block[1:]] = FlipFlop(block[1:], outputs.split(", "))
            elif block[0] == "&":
                conjunctions[block[1:]] = outputs.split(", ")
                components[block[1:]] = Conjunction(block[1:], outputs.split(", "))
    for name, outputs in components.items():
        for output in outputs.connections:
            if output in conjunctions:
                components[output].inputs.append(name)
    for output in broadcaster:
        if output in conjunctions:
            components[output].inputs.append("broadcaster")

    for name, comp in components.items():
        comp.initialize()

    count = 0
    while True:
        count += 1
        pulses = [(c, "broadcaster", False) for c in broadcaster]
        while len(pulses) > 0:
            for p in pulses:
                if p[0] == "rx" and p[2] == False:
                    return count
            new_pulses = []
            for pulse in pulses:
                if pulse[0] in components:
                    new_pulses.extend(components[pulse[0]].receive_pulse(pulse[1], pulse[2]))

            pulses = new_pulses


def part2_v2(fname="day20_input.txt"):
    components = {}
    broadcaster = None
    flipflops = {}
    conjunctions = {}
    with open(fname, "r") as f:
        lines = f.readlines()
        for line in lines:
            block, outputs = line[:-1].split(" -> ")
            if block == "broadcaster":
                broadcaster = outputs.split(", ")
            elif block[0] == "%":
                flipflops[block[1:]] = outputs.split(", ")
                components[block[1:]] = FlipFlop(block[1:], outputs.split(", "))
            elif block[0] == "&":
                conjunctions[block[1:]] = outputs.split(", ")
                components[block[1:]] = Conjunction(block[1:], outputs.split(", "))
    for name, outputs in components.items():
        for output in outputs.connections:
            if output in conjunctions:
                components[output].inputs.append(name)
    for output in broadcaster:
        if output in conjunctions:
            components[output].inputs.append("broadcaster")

    for name, comp in components.items():
        comp.initialize()

    count = 0
    while True:
        if len(components["qn"].debug) > 0:
            print(count, components["qn"].debug)
            components["qn"].debug = []
        #for k, v in components["qn"].prev_pulses.items():
        #    if v:
        #        print(k, count)
        count += 1
        pulses = [(c, "broadcaster", False) for c in broadcaster]
        while len(pulses) > 0:
            for p in pulses:
                if p[0] == "rx" and p[2] == False:
                    return count
            new_pulses = []
            for pulse in pulses:
                if pulse[0] in components:
                    new_pulses.extend(components[pulse[0]].receive_pulse(pulse[1], pulse[2]))

            pulses = new_pulses


#print(part1(fname="day20_test.txt"))
#print(part1(fname="day20_test2.txt"))
#print(part1(fname="day20_input.txt"))
#print(part2(fname="day20_test.txt"))
#print(part2(fname="day20_test2.txt"))
#print(part2(fname="day20_input.txt"))
print(part2_v2(fname="day20_input.txt"))
