def p1(inp):
    result = 0
    for idx in range(1, len(inp)):
        if inp[idx] > inp[idx - 1]:
            result += 1
    return result


def p2(inp):
    result = 0
    for idx in range(1, len(inp) - 2):
        if inp[idx + 2] > inp[idx - 1]:
            result += 1
    return result


with open('../../input/week1/day1.txt') as file:
    inp = []
    for line in file:
        inp.append(int(line))

    print('part 1: ' + str(p1(inp)))
    print('part 2: ' + str(p2(inp)))
