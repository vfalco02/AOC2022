import aocd

input_ = aocd.get_data(day=3, year=2022)

# input_ = '''vJrwpWtwJgWrhcsFMMfFFhFp
# jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
# PmmdzqPrVvPwwTWBwg
# wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
# ttgJtRGJQctTZtZT
# CrZsJsPPZsGzwwsLwLmpwMDw'''

rucksacks = input_.splitlines()


def get_letter_value(letter):
    if 65 <= ord(letter) <= 90:
        return ord(letter) - 38
    else:
        return ord(letter) - 96


def part1():
    total = 0
    for sack in rucksacks:
        middle = len(sack)//2
        comp1 = sorted(sack[:middle])
        comp2 = sorted(sack[middle:])
        same = [x for x in set(comp1).intersection(set(comp2))][0]
        total += get_letter_value(same)
    print(total)


def part2():
    groups = []
    temp = [rucksacks[0]]
    for sack in rucksacks:
        if rucksacks.index(sack) == 0:
            continue
        if rucksacks.index(sack) % 3 != 0:
            temp.append(sack)
        else:
            groups.append(temp)
            temp = [sack]
    else:
        groups.append(temp)

    total = 0
    for group in groups:
        common = [x for x in set(group[0]).intersection(group[1]).intersection(group[2])][0]
        total += get_letter_value(common)
    print(total)


if __name__ == "__main__":
    part1()
    part2()
