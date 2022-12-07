import aocd


class DirectoryNode:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = []

    @property
    def size(self):
        total = 0
        total += self.sum_files_in_dir(total=total)
        return total

    def sum_files_in_dir(self, directory=None, total=0):
        directory = self if directory is None else directory
        for child in directory.children:
            if isinstance(child, FileNode):
                total += child.size
            elif isinstance(child, DirectoryNode):
                total = self.sum_files_in_dir(child, total)
        return total


class FileNode:
    def __init__(self, name, parent, size):
        self.name = name
        self.parent = parent
        self.size = size


input_ = aocd.get_data(day=7, year=2022)

# input_ = '''$ cd /
# $ ls
# dir a
# 14848514 b.txt
# 8504156 c.dat
# dir d
# $ cd a
# $ ls
# dir e
# 29116 f
# 2557 g
# 62596 h.lst
# $ cd e
# $ ls
# 584 i
# $ cd ..
# $ cd ..
# $ cd d
# $ ls
# 4060174 j
# 8033020 d.log
# 5626152 d.ext
# 7214296 k'''

lines = input_.splitlines()
directories = []


def do_cd(current_dir, command):
    command = command.replace("$ ", '')
    directory = command.split(' ')[1]
    if directory == "..":
        return current_dir.parent
    dir_node = DirectoryNode(directory, current_dir)
    directories.append(dir_node)
    if current_dir:
        current_dir.children.append(dir_node)
    return dir_node


def record_file(current_dir, file_line):
    size, name = file_line.split(' ')
    file_node = FileNode(name, current_dir, int(size))
    return file_node


def part1():
    current_directory = None
    for line in lines:
        if '$ cd' in line:
            current_directory = do_cd(current_directory, line)
        elif '$ ls' in line or line[0:3] == "dir":
            continue
        else:
            file = record_file(current_directory, line)
            current_directory.children.append(file)
    print(sum([x.size for x in directories if x.size <= 100000]))


def part2():
    space_unused = 70000000 - directories[0].size
    print(f'unused: {space_unused}')
    space_needed = 30000000
    print(f'needed: {space_needed}')
    space_to_free_up = space_needed - space_unused
    print(f'to free up: {space_to_free_up}')
    candidates = {x.name: x.size for x in directories if x.size >= space_to_free_up}
    print(min(candidates.values()))


if __name__ == "__main__":
    part1()
    part2()



