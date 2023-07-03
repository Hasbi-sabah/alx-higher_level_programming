#!/usr/bin/python3
from sys import argv
def check_if_safe(i, j, board):
    for element in board:
        if i == element[0] or j == element[1] or abs(i - element[0]) == abs(j - element[1]):
                return False
    return True

def check_if_not_done(i, j, big_board):
    for board in big_board:
        if len(board) > i and i == board[i][0] and j == board[i][1]:
                return False
    return True

if len(argv) != 2:
    print('Usage: nqueens N')
    exit(1)
if not argv[1].isdigit():
    print('N must be a number')
    exit(1)
n = int(argv[1])
if n < 4:
    print('N must be at least 4')
    exit(1)
big_board = []
for a in range(n):
    board = []
    for i in range(n):
        for j in range(n):
            if check_if_not_done(i, j, big_board) and check_if_safe(i, j, board):
                board.append([i, j])
    big_board.append(board)
    if len(board) == n:
        print(board)
