import aocd

input_ = aocd.get_data(day=5, year=2022)

# input_ = '''    [D]
# [N] [C]
# [Z] [M] [P]
#  1   2   3
#
# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2'''


def get_crates_and_moves():
    crates, moves = input_.split('\n\n')
    crates = crates.splitlines()
    cols = int(crates[-1].split("   ")[-1])
    crates = [[row[i-3:i] for row in crates[:-1] if row[i-3:i] != "   "] for i in range(3,cols*4+1, 4)]
    moves = [move.replace('move ', '').replace(' from ', '-').replace(' to ', '-') for move in moves.splitlines()]
    return crates, moves


def part1():
    crates, moves = get_crates_and_moves()
    for move in moves:
        amount, from_, to = move.split('-')
        from_ = int(from_) - 1
        to = int(to) - 1
        temp = crates[from_][:int(amount)]
        temp.reverse()
        crates[from_] = crates[from_][int(amount):]
        crates[to] = temp + crates[to]
    print(''.join([i[0] for i in crates if len(i) > 0]).replace('[', '').replace(']', ''))


def part2():
    crates, moves = get_crates_and_moves()
    for move in moves:
        amount, from_, to = move.split('-')
        from_ = int(from_) - 1
        to = int(to) - 1
        temp = crates[from_][:int(amount)]
        crates[from_] = crates[from_][int(amount):]
        crates[to] = temp + crates[to]
    print(''.join([i[0] for i in crates if len(i) > 0]).replace('[', '').replace(']', ''))


if __name__ == "__main__":
    part1()
    part2()