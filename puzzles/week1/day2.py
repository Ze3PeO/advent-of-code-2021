def p1(inp):
    hpos = depth = 0

    for line in inp:
        split = line.split()
        if split[0] == 'forward':
            hpos += int(split[1])
        elif split[0] == 'up':
            depth -= int(split[1])
        elif split[0] == 'down':
            depth += int(split[1])

    return hpos * depth


def p2(inp):
    hpos = depth = aim = 0

    for line in inp:
        split = line.split()
        if split[0] == 'forward':
            hpos += int(split[1])
            depth += int(split[1]) * aim
        elif split[0] == 'up':
            aim -= int(split[1])
        elif split[0] == 'down':
            aim += int(split[1])

    return hpos * depth


with open('../../input/week1/day2.txt') as f:
    inp = f.readlines()

    print('part 1: ' + str(p1(inp)))
    print('part 2: ' + str(p2(inp)))