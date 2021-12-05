INP_WIDTH = 12


def p1(inp):
    count = [0] * INP_WIDTH
    gamma_rate = 0

    for num in inp:
        for idx, char in enumerate(num):
            count[idx] += 1 if int(char) == 0 else -1

    for idx in range(0, len(count)):
        gamma_rate += pow(2, len(count) - 1 - idx) if count[idx] > 0 else 0

    epsilon_rate = ~gamma_rate & pow(2, len(count)) - 1

    return gamma_rate * epsilon_rate


def p2(inp):
    o2_gen_rating = calc_ratings(inp, 1, 0)
    co2_scrub_rating = calc_ratings(inp, 0, 1)

    return o2_gen_rating * co2_scrub_rating


def calc_ratings(inp, val_for_one_majority, val_for_zero_majority):
    result = 0

    candidates = inp.copy()
    results = []

    for idx in range(INP_WIDTH):
        count = 0
        for num in candidates:
            count += 1 if int(num[idx]) == 1 else -1
        count = val_for_one_majority if count >= 0 else val_for_zero_majority
        for num in candidates:
            if int(num[idx]) == count:
                results.append(num)
        if len(results) == 1:
            result = int(results[0], 2)
            break
        candidates = results.copy()
        results = []

    return result


with open('../../input/week1/day3.txt') as file:
    inp = []
    for line in file:
        inp.append(line.strip())

    print('part 1: ' + str(p1(inp)))
    print('part 2: ' + str(p2(inp)))
