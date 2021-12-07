import sys

import numpy as np


def p1(inp):
    fuel = 0
    med = np.median(inp)

    for crab in inp:
        fuel += abs(med - crab)

    return fuel


def p2(inp):
    #fuel_floor = fuel_ceil = 0
    #mean = np.mean(inp)
    #mean_floor = math.floor(mean)
    #mean_ceil = math.ceil(mean)
    #for crab in inp:
    #    dist_floor = abs(mean_floor - crab)
    #    fuel_floor += (dist_floor * (dist_floor + 1)) / 2
    #    dist_ceil = abs(mean_ceil - crab)
    #    fuel_ceil += (dist_ceil * (dist_ceil + 1)) / 2
    #return min(fuel_floor, fuel_ceil)

    fuel = sys.maxsize
    for num in range(min(inp), max(inp)):
        temp_fuel = 0
        for crab in inp:
            dist = abs(num - crab)
            temp_fuel += (dist * (dist + 1)) / 2
        if temp_fuel < fuel:
            fuel = temp_fuel

    return fuel


with open('../../input/week1/day7.txt') as file:
    inp = [int(num) for num in file.readline().split(",")]

    print('part 1: ' + str(p1(inp)))
    print('part 2: ' + str(p2(inp)))
