def parse_input(fname="day7_input.txt"):
    with open(fname, "r") as f:
        lines = f.readlines()
        commands = []
        for line in lines:
            if line[0] == '$':  # Command
                if line[2:4] == "cd":
                    commands.append(("cd", line[4:].strip()))
                elif line[2:4] == "ls":
                    commands.append(("ls", []))
                else:
                    raise NotImplementedError
            else:  # Output
                commands[-1][1].append(line.strip())

    return commands


def parse_ls(data):
    info, name = data.split(" ")
    if info == "dir":
        return name, {"..": name}
    else:
        return name, int(info)


class Filesystem:

    def __init__(self):

        self.cur_dir = ["/"]
        self.structure = {"/": {"..": "/"}}
        self.sub_dir = self.structure
        self.sizes = {}

    def cd(self, command):
        if command == "..":
            self.cur_dir.pop()
        elif command == "/":
            self.cur_dir = ["/"]
        else:
            self.cur_dir.append(command)


    def ls(self, results):
        for result in results:
            name, contents = parse_ls(result)
            # print(self.structure)
            # print(f"{self.cur_dir=}")
            # print("")
            sub_dir = self.structure
            for dir_step in self.cur_dir:
                sub_dir = sub_dir[dir_step] 
            sub_dir[name] = contents

    def get_directory_sizes(self):
        self.get_directory_size(cur_path="/", sub_dir=self.structure)
        return self.sizes

    def get_directory_size(self, cur_path, sub_dir):
        if type(sub_dir) == int:
            return sub_dir
        size = 0
        for file_name, value in sub_dir.items():
            if file_name == "..":
                continue
            size += self.get_directory_size(cur_path=cur_path + "/" + file_name, sub_dir=value)
        self.sizes[cur_path] = size
        return size


def get_sizes(fname="day7_input.txt"):
    commands = parse_input(fname=fname)
    fs = Filesystem()

    for command in commands:
        if command[0] == "cd":
            fs.cd(command[1])
        elif command[0] == "ls":
            fs.ls(command[1])
        else:
            raise NotImplementedError

    return fs.get_directory_sizes()

def part1(fname="day7_input.txt"):
    sizes = get_sizes(fname=fname)
    total = 0
    for key, value in sizes.items():
        if value <= 100000:
            total += value
    return total

def part2(fname="day7_input.txt"):
    sizes = get_sizes(fname=fname)
    used_space = sizes["/"]
    total_space = 70000000
    space_needed = 30000000
    space_left = total_space - used_space
    space_to_free = space_needed - space_left

    space_to_delete = used_space

    for key, value in sizes.items():
        if value >= space_to_free and value < space_to_delete:
            space_to_delete = value
    return space_to_delete


print(part1())
print(part2())
