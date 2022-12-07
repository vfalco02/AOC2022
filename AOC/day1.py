import aocd
import heapq

input_ = aocd.get_data(day=1, year=2022)
elves = [
    [int(line) for line in calories.splitlines()]
    for calories in input_.split('\n\n')
]


if __name__ == "__main__":
    print(f"Part 1: {max(elves)}")
    print(f"Part 2: {sum(heapq.nlargest(3, (sum(elf) for elf in elves)))}")