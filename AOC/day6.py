import aocd

input_ = aocd.get_data(day=6, year=2022)

# input_ = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"


def find_distinct(char_count):
    index = char_count - 1
    for i in range(index, len(input_)):
        chunk = input_[i-index:i+1]
        if len(set(chunk)) == char_count:
            print(i+1)
            break


def part1():
    find_distinct(4)


def part2():
    find_distinct(14)


if __name__ == "__main__":
    part1()
    part2()
