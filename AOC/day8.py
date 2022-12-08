import aocd

input_ = aocd.get_data(day=8, year=2022)

# input_ = '''30373
# 25512
# 65332
# 33549
# 35390'''

rows = [list(row) for row in input_.splitlines()]
rows = [[int(tree) for tree in row] for row in rows]


def is_visible(tree, subset):
    return True if tree > max(subset) else False


def part1():
    visible = len(rows[0]) + len(rows[-1]) + len([row[0] for row in rows[1:-1]]) + len([row[-1] for row in rows[1:-1]])
    cols = [[row[i] for row in rows] for i in range(len(rows))]
    for i in range(1, len(rows[1:])):
        for j in range(1, len(rows[i])-1):
            tree = rows[i][j]
            can_be_seen = (
                is_visible(tree, rows[i][j + 1:]),
                is_visible(tree, rows[i][0:j]),
                is_visible(tree, cols[j][0:i]),
                is_visible(tree, cols[j][i+1:])
            )
            visible += 1 if any(can_be_seen) else 0
    print(visible)


def count_view(tree, subset):
    count = 0
    for height in subset:
        if tree > height:
            count += 1
        elif tree <= height:
            count += 1
            break
        else:
            break
    return count


def part2():
    scores = []
    cols = [[row[i] for row in rows] for i in range(len(rows))]
    for i in range(1, len(rows[1:])):
        for j in range(1, len(rows[i])-1):
            tree = rows[i][j]
            right, left, up, down = (
                count_view(tree, rows[i][j+1:]),
                count_view(tree, reversed(rows[i][:j])),
                count_view(tree, reversed(cols[j][:i])),
                count_view(tree, cols[j][i+1:])
            )
            score = right*left*up*down
            scores.append(score)
    print(max(scores))


if __name__ == "__main__":
    part1()
    part2()
