import aocd

input_ = aocd.get_data(day=10, year=2022)

def part1():
    X = 1
    cycle = 1
    signal = 0
    prev_X = 0
    for command in input_.splitlines():
        if "noop" in command:
            cycle += 1
        else:
            value = int(command.split(' ')[1])
            prev_X = X
            X += value
            cycle += 2
        if cycle in [20, 60, 100, 140, 180, 220]:
            signal += cycle * X
        elif cycle in [21, 61, 101, 141, 181, 221] and "addx" in command:
            signal += (cycle-1) * prev_X
    print(signal)


class Commands:
    def __init__(self, commands):
        self.commands = commands.splitlines()
        self.cur_index = 0

    @property
    def has_next(self):
        if self.cur_index == len(self.commands):
            return False
        return True

    def get_next(self):
        if self.cur_index == len(self.commands):
            return None
        self.cur_index += 1
        return self.commands[self.cur_index - 1]


def part2():
    cycle_time = {"noop": 1, "addx": 2}
    crt = [["." for i in range(40)] for j in range(6)]
    row, col = 0, 0
    sprite = 0
    commands = Commands(input_)
    while commands.has_next:
        cmd = commands.get_next()
        op = cmd.split(' ')[0]
        for i in range(cycle_time[op]):
            if sprite <= row <= sprite + 2:
                crt[col][row] = "#"
            row = row + 1 if row + 1 < 40 else 0
            col = col + 1 if row == 0 else col
        if op == "addx":
            sprite += int(cmd.split(' ')[1])



    crt = [''.join(row) for row in crt]
    print('\n'.join(crt))


if __name__ == "__main__":
    part1()
    part2()