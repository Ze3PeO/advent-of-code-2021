import numpy as np


def p1():
    paper_height, paper_width = base_paper_height, base_paper_width
    field = np.zeros((paper_height, paper_width))
    for x, y in coords:
        field[y][x] = 1

    axis, lines = instructions[0]
    field, paper_height, paper_width = execute_instruct(axis, field, lines, paper_height, paper_width)

    return field.sum()


def p2():
    paper_height, paper_width = base_paper_height, base_paper_width
    field = np.empty((paper_height, paper_width))
    for x, y in coords:
        field[y][x] = 1

    for axis, lines in instructions:
        field, paper_height, paper_width = execute_instruct(axis, field, lines, paper_height, paper_width)

    print(field)

    return 0


def execute_instruct(axis, field, lines, paper_height, paper_width):
    if axis == 'x':
        for y in range(paper_height):
            for x in range(paper_width - 1, lines, -1):
                if field[y][x] == 1:
                    field[y][2 * lines - x] = 1
        paper_width = lines
        field = field[:paper_height, :paper_width]
    elif axis == 'y':
        for x in range(paper_width):
            for y in range(paper_height - 1, lines, -1):
                if field[y][x] == 1:
                    field[2 * lines - y][x] = 1
        paper_height = lines
        field = field[:paper_height, :paper_width]
    return field, paper_height, paper_width


with open('../../input/week2/day13.txt') as file:
    coords = []
    instructions = []
    base_paper_width = base_paper_height = -1
    for line in file.readlines():
        if line == '\n':
            continue
        if line.startswith('fold'):
            instruct = line.strip().split(' ')[2].strip().split('=')
            instructions.append((instruct[0], int(instruct[1])));
        else:
            coord = line.strip().split(',')
            coords.append((int(coord[0]), int(coord[1])))
            if int(coord[0]) > base_paper_width:
                base_paper_width = int(coord[0])
            if int(coord[1]) > base_paper_height:
                base_paper_height = int(coord[1])
    base_paper_width += 1
    base_paper_height += 1

    print('part 1: ' + str(p1()))
    print('part 2: ' + str(p2()))
