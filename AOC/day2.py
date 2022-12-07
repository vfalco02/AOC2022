import aocd

input_ = aocd.get_data(day=2, year=2022)

hands = {"A": "R", "B": "P", "C": "S"}
beats = {"R": "S", "S": "P", "P": "R"}
points = {"R": 1, "P": 2, "S": 3}
needs_to = {"X": "L", "Y": "D", "Z": "W"}
for hand, value in hands.items():
    input_ = input_.replace(hand, value)

rounds = input_.splitlines()
total = 0

for round_ in rounds:
    opponent, wld = round_.split(" ")
    if needs_to[wld] == "D":
        total += 3 + points[opponent]
    elif needs_to[wld] == "L":
        total += points[beats[opponent]]
    else:
        mine = [key for key, val in beats.items() if val == opponent][0]
        total += 6 + points[mine]


if __name__ == "__main__":
    print(total)
