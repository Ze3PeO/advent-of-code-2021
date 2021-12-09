def p1():
    count = 0
    for y, x in calc_low_points():
        count += field[y][x] + 1
    return count


def p2():
    basin_size = {}
    basin_count = 0

    for y, x in calc_low_points():
        basin_size[basin_count] = 0
        fill4(x, y, basin_size, basin_count)
        basin_count += 1

    sizes = list(basin_size.values())
    sizes.sort()
    return sizes[-1] * sizes[-2] * sizes[-3]


def calc_low_points():
    low_points = []
    for y in range(field_height):
        for x in range(field_width):
            if y - 1 >= 0 and field[y][x] >= field[y - 1][x]:               # oben
                continue
            if y + 1 < field_height and field[y][x] >= field[y + 1][x]:     # unten
                continue
            if x - 1 >= 0 and field[y][x] >= field[y][x - 1]:               # links
                continue
            if x + 1 < field_width and field[y][x] >= field[y][x + 1]:      # rechts
                continue
            low_points.append((y, x))
    return low_points


def fill4(x, y, basin_size, basin_count):
    if field[y][x] == 9:
        return

    field[y][x] = 9
    basin_size[basin_count] += 1

    if y - 1 >= 0:
        fill4(x, y - 1, basin_size, basin_count)    # oben
    if y + 1 < field_height:
        fill4(x, y + 1, basin_size, basin_count)    # unten
    if x - 1 >= 0:
        fill4(x - 1, y, basin_size, basin_count)    # links
    if x + 1 < field_width:
        fill4(x + 1, y, basin_size, basin_count)    # rechts


def parse_input():
    global field, field_height, field_width

    field = []
    for line in file.readlines():
        row = [int(num) for num in list(line.strip())]
        field.append(row)

    field_height = len(field)
    field_width = len(field[0])


with open('../../input/week2/day9.txt') as file:
    parse_input()

    print('part 1: ' + str(p1()))
    print('part 2: ' + str(p2()))
