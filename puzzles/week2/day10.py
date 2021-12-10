import math


opening = ['(', '[', '{', '<']
closing = [')', ']', '}', '>']
pairs = {')': '(', ']': '[', '}': '{', '>': '<'}
points_p1 = {')': 3, ']': 57, '}': 1197, '>': 25137}
points_p2 = {'(': 1, '[': 2, '{': 3, '<': 4}


def p1(lines):
    result = 0

    for line in lines:
        stack = []
        for char in line:
            if char in opening:
                stack.append(char)
            if char in closing:
                to_close = stack.pop()
                if pairs[char] != to_close:
                    result += points_p1[char]
                    break

    return result


def p2(lines):
    scores = []

    for line in lines:
        stack = []
        valid = True
        for char in line:
            if char in opening:
                stack.append(char)
            if char in closing:
                to_close = stack.pop()
                if pairs[char] != to_close:
                    valid = False
                    break
        if valid:
            score = 0
            for i in range(len(stack)):
                score *= 5
                score += points_p2[stack.pop()]
            scores.append(score)
    scores.sort()

    return scores[math.floor(len(scores) / 2)]


with open('../../input/week2/day10.txt') as file:
    lines = file.readlines()

    print('part 1: ' + str(p1(lines)))
    print('part 2: ' + str(p2(lines)))
