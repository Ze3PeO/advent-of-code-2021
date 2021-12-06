def p1(inp):
    return count_fish(80)


def p2(inp):
    return count_fish(256)


def count_fish(days):
    dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
    for num in inp:
        dict[num] += 1

    for day in range(days):
        temp_dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
        for key, value in dict.items():
            if key == 0:
                temp_dict[6] += value
                temp_dict[8] += value
            else:
                temp_dict[(key - 1)] += value
        dict = temp_dict

    return sum(dict.values())


with open('../../input/week1/day6.txt') as file:
    inp = [int(num) for num in file.readline().split(",")]

    print('part 1: ' + str(p1(inp)))
    print('part 2: ' + str(p2(inp)))
