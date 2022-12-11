import math

import aocd

input_ = aocd.get_data(day=11, year=2022)
# input_ = '''Monkey 0:
#   Starting items: 79, 98
#   Operation: new = old * 19
#   Test: divisible by 23
#     If true: throw to monkey 2
#     If false: throw to monkey 3
#
# Monkey 1:
#   Starting items: 54, 65, 75, 74
#   Operation: new = old + 6
#   Test: divisible by 19
#     If true: throw to monkey 2
#     If false: throw to monkey 0
#
# Monkey 2:
#   Starting items: 79, 60, 97
#   Operation: new = old * old
#   Test: divisible by 13
#     If true: throw to monkey 1
#     If false: throw to monkey 3
#
# Monkey 3:
#   Starting items: 74
#   Operation: new = old + 3
#   Test: divisible by 17
#     If true: throw to monkey 0
#     If false: throw to monkey 1'''


class Monkey:
    def __init__(self, raw_input):
        data = raw_input.splitlines()
        self.items = data[1].split(': ')[1]
        self.items = [int(item) for item in self.items.split(', ')]
        self.operation = data[2].split('= ')[1]
        self.test = int(data[3].split('by ')[1])
        self.true = int(data[4].split('monkey ')[1])
        self.false = int(data[5].split('monkey ')[1])
        self.inspected = 0

    def do_turn(self, monkeys, supermod=None):
        for i in range(len(self.items)):
            if supermod:
                old = self.items[i]
                new = eval(self.operation)
                new = new % supermod
            else:
                old = self.items[i]
                new = math.floor(eval(self.operation) / 3)
            if new % self.test == 0:
                monkeys[self.true].items.append(new)
            else:
                monkeys[self.false].items.append(new)
            self.inspected += 1
        self.items = []


def part1():
    monkeys = [Monkey(monkey) for monkey in input_.split('\n\n')]
    for i in range(20):
        for monkey in monkeys:
            monkey.do_turn(monkeys)
    inspections = sorted([monkey.inspected for monkey in monkeys])
    print(inspections[-2]*inspections[-1])


def part2():
    monkeys = [Monkey(monkey) for monkey in input_.split('\n\n')]
    supermod = 1
    for monkey in monkeys:
        supermod *= monkey.test
    for i in range(10000):
        for monkey in monkeys:
            monkey.do_turn(monkeys, supermod)
    inspections = sorted([monkey.inspected for monkey in monkeys])
    print(inspections[-2]*inspections[-1])


if __name__ == "__main__":
    part1()
    part2()