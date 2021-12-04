import re


BOARD_WIDTH = 5
BOARD_HEIGHT = 5


def p1(numbers, boards):
    for num in numbers:
        for board in boards:
            for y in range(BOARD_HEIGHT):
                for x in range(BOARD_WIDTH):
                    if board[y][x] == num:
                        board[y][x] = -1
            if check_for_win(board):
                return calc_result(board, num)

    return -1


def p2(numbers, boards):
    for num in numbers:
        to_remove = []
        for board in boards:
            for y in range(BOARD_HEIGHT):
                for x in range(BOARD_WIDTH):
                    if board[y][x] == num:
                        board[y][x] = -1
            if check_for_win(board):
                to_remove.append(board)
        for board in to_remove:
            if len(boards) == 1:
                return calc_result(boards.pop(), num)
            boards.remove(board)

    return -1


def check_for_win(board):
    for y in range(BOARD_HEIGHT):
        tileCount = 0
        for x in range(BOARD_WIDTH):
            tileCount += board[y][x]
        if tileCount == -BOARD_WIDTH:
            return True

    for x in range(BOARD_WIDTH):
        tileCount = 0
        for y in range(BOARD_HEIGHT):
            tileCount += board[y][x]
        if tileCount == -BOARD_WIDTH:
            return True

    return False


def calc_result(board, num):
    result = 0

    for x in range(BOARD_WIDTH):
        for y in range(BOARD_HEIGHT):
            if board[y][x] != -1:
                result += board[y][x]

    return result * num


def parse_input(inp):
    numbers = inp.pop(0).rstrip().split(",")
    numbers = [int(num) for num in numbers]

    whitespace_idx = 0
    while whitespace_idx < len(inp):
        inp.pop(whitespace_idx)
        whitespace_idx += BOARD_HEIGHT

    boards = []

    for idx in range(0, len(inp), BOARD_HEIGHT):
        board = []
        for y in range(BOARD_HEIGHT):
            row = re.sub(" +", " ", inp[idx + y]).strip().split(" ")
            row = [int(tile) for tile in row]
            board.append(row)
        boards.append(board)

    return numbers, boards


with open('../../input/week1/day4.txt') as file:
    inp = file.readlines()

    numbers, boards = parse_input(inp)

    print('part 1: ' + str(p1(numbers, boards)))
    print('part 2: ' + str(p2(numbers, boards)))