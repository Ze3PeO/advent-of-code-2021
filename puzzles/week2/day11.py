import numpy as np

FIELD_DIMEN = 10


def p1(inp):
    global field, has_flashed

    field = [row[:] for row in inp]
    result = 0

    for step in range(100):
        has_flashed = np.zeros((FIELD_DIMEN, FIELD_DIMEN), dtype=bool)

        for y in range(FIELD_DIMEN):
            for x in range(FIELD_DIMEN):
                increase(x, y)

        result += has_flashed.sum()

    return result


def p2(inp):
    global field, has_flashed

    field = [row[:] for row in inp]
    steps = 0
    synchronized = False

    while not synchronized:
        has_flashed = np.zeros((FIELD_DIMEN, FIELD_DIMEN), dtype=bool)

        for y in range(FIELD_DIMEN):
            for x in range(FIELD_DIMEN):
                increase(x, y)

        steps += 1

        if has_flashed.sum() == FIELD_DIMEN * FIELD_DIMEN:
            synchronized = True

    return steps


def increase(x, y):
    if not has_flashed[y][x]:
        field[y][x] += 1

    if field[y][x] > 9:
        flash(x, y)


def flash(x, y):
    if has_flashed[y][x]:
        return

    has_flashed[y][x] = True
    field[y][x] = 0

    for j in range(y - 1, y + 2):
        for i in range(x - 1, x + 2):
            if is_within_bounds(i, j) and (j != y or i != x):
                increase(i, j)


def is_within_bounds(x, y):
    if 0 <= y < FIELD_DIMEN and 0 <= x < FIELD_DIMEN:
        return True
    return False


with open('../../input/week2/day11.txt') as file:
    inp = []
    for line in file.readlines():
        row = [int(num) for num in list(line.strip())]
        inp.append(row)

    print('part 1: ' + str(p1(inp)))
    print('part 2: ' + str(p2(inp)))
