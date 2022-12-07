import aocd

input_ = aocd.get_data(day=4, year=2022)

# input_ = '''2-4,6-8
# 2-3,4-5
# 5-7,7-9
# 2-8,3-7
# 6-6,4-6
# 2-6,4-8'''

pairs = input_.splitlines()

def part1():
    count = 0
    for pair in pairs:
        pair1, pair2 = pair.split(',')
        start1, end1 = pair1.split('-')
        start2, end2 = pair2.split('-')
        pair1 = list(range(int(start1), int(end1)+1))
        pair2 = list(range(int(start2), int(end2)+1))
        if set(pair1).issuperset(pair2) or set(pair1).issubset(pair2):
            count += 1
    print(count)


def part2():
    count = 0
    for pair in pairs:
        pair1, pair2 = pair.split(',')
        start1, end1 = pair1.split('-')
        start2, end2 = pair2.split('-')
        pair1 = list(range(int(start1), int(end1)+1))
        pair2 = list(range(int(start2), int(end2)+1))
        if set(pair1).intersection(pair2) != set():
            count += 1
    print(count)


if __name__ == "__main__":
    part1()
    part2()