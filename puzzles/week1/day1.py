def p1(inp):
    result = 0
    for i in range(1, len(inp)):
        if inp[i] > inp[i - 1]:
            result += 1
    return result


def p2(inp):
    result = 0
    for i in range(1, len(inp) - 2):
        if inp[i + 2] > inp[i - 1]:
            result += 1
    return result


with open('../input/week1/day1.txt') as f:
    inp = []
    for line in f:
        inp.append(int(line))

    print('part 1: ' + str(p1(inp)))
    print('part 2: ' + str(p2(inp)))