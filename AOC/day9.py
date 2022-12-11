import aocd

input_ = aocd.get_data(day=9, year=2022)

# input_ = '''R 5
# U 8
# L 8
# D 3
# R 17
# D 10
# L 25
# U 20'''


class Head:
    def __init__(self):
        self.x, self.y = 0, 0

    def _move(self, x, y):
        self.x += x
        self.y += y

    def move_left(self):
        self._move(-1, 0)

    def move_right(self):
        self._move(1, 0)

    def move_up(self):
        self._move(0, -1)

    def move_down(self):
        self._move(0, 1)


class Knot:
    def __init__(self, ahead):
        self.ahead = ahead
        self.x = 0
        self.y = 0

    @property
    def is_adjacent(self):
        if -1 <= self.x - self.ahead.x <= 1 and -1 <= self.y - self.ahead.y <= 1:
            return True
        return False

    def move_adjacent(self):
        if not self.is_adjacent:
            if abs(self.ahead.x - self.x) == 2:
                if abs(self.ahead.y - self.y) != 2:
                    self.y = self.ahead.y
                if self.ahead.x > self.x:
                    self.x += 1
                elif self.ahead.x < self.x:
                    self.x -= 1
            else:
                self.x = self.ahead.x
            if abs(self.ahead.y - self.y) == 2:
                if self.ahead.y > self.y:
                    self.y += 1
                elif self.ahead.y < self.y:
                    self.y -= 1
            else:
                self.y = self.ahead.y

        return self.x, self.y


def part1():
    h = Head()
    t = Knot(h)

    methods = {
        "R": h.move_right,
        "L": h.move_left,
        "U": h.move_up,
        "D": h.move_down
    }

    head_coords = []
    tail_coords = []
    for directions in input_.splitlines():
        direction = directions[0]
        steps = directions[2:]
        for step in range(int(steps)):
            methods[direction]()
            t.move_adjacent()
            head_coords.append((h.x, h.y))
            tail_coords.append((t.x, t.y))

    print(f"Part 1: {len(set(tail_coords))}")


def part2():
    h = Head()
    k1 = Knot(h)
    k2 = Knot(k1)
    k3 = Knot(k2)
    k4 = Knot(k3)
    k5 = Knot(k4)
    k6 = Knot(k5)
    k7 = Knot(k6)
    k8 = Knot(k7)
    k9 = Knot(k8)
    knots = [k1, k2, k3, k4, k5, k6, k7, k8, k9]
    methods = {
        "R": h.move_right,
        "L": h.move_left,
        "U": h.move_up,
        "D": h.move_down
    }

    tail_coords = []
    for directions in input_.splitlines():
        direction = directions[0]
        steps = directions[2:]
        for step in range(int(steps)):
            methods[direction]()
            for knot in knots:
                knot.move_adjacent()
            tail_coords.append((k9.x, k9.y))

    print(f"Part 2: {len(set(tail_coords))}")


if __name__ == "__main__":
    part1()
    part2()
