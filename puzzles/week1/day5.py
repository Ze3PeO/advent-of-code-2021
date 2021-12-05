import numpy as np

FIELD_DIMEN = 990


def p1(lines):
    field = np.zeros((FIELD_DIMEN, FIELD_DIMEN))

    for line in lines:
        if line[0][0] == line[1][0] or line[0][1] == line[1][1]:
            points = bresenham(line[0], line[1])
            for point in points:
                field[point[1]][point[0]] += 1

    return calc_overlaps(field)


def p2(lines):
    field = np.zeros((FIELD_DIMEN, FIELD_DIMEN))

    for line in lines:
        points = bresenham(line[0], line[1])
        for point in points:
            field[point[1]][point[0]] += 1

    return calc_overlaps(field)


def calc_overlaps(field):
    result = 0

    for row in field:
        for tile in row:
            if tile >= 2:
                result += 1

    return result


# Bresenham line algorithm borrowed from: https://www.codegrepper.com/code-examples/python/python+bresenham+line+algorithm
def bresenham(start, end):
    # Setup initial conditions
    x1, y1 = start
    x2, y2 = end
    dx = x2 - x1
    dy = y2 - y1

    # Determine how steep the line is
    is_steep = abs(dy) > abs(dx)

    # Rotate line
    if is_steep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    # Swap start and end points if necessary and store swap state
    swapped = False
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        swapped = True

    # Recalculate differentials
    dx = x2 - x1
    dy = y2 - y1

    # Calculate error
    error = int(dx / 2.0)
    ystep = 1 if y1 < y2 else -1

    # Iterate over bounding box generating points between start and end
    y = y1
    points = []
    for x in range(x1, x2 + 1):
        coord = (y, x) if is_steep else (x, y)
        points.append(coord)
        error -= abs(dy)
        if error < 0:
            y += ystep
            error += dx

    # Reverse the list if the coordinates were swapped
    if swapped:
        points.reverse()
    return points


def parse_input(inp):
    lines = []

    for elem in inp:
        coord_pairs = elem.rstrip().split(" -> ")
        x = [int(num) for num in coord_pairs[0].split(",")]
        y = [int(num) for num in coord_pairs[1].split(",")]
        line = [x, y]
        lines.append(line)

    return lines


with open('../../input/week1/day5.txt') as file:
    inp = file.readlines()

    lines = parse_input(inp)

    print('part 1: ' + str(p1(lines)))
    print('part 2: ' + str(p2(lines)))
