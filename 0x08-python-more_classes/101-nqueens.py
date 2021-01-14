#!/usr/bin/python3
"""Back tracking Method"""
import sys


def check_argv():
    """checks agrv for errors"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    num = 0

    if sys.argv[1].isdigit():
        num = int(sys.argv[1])
        if num is int:
            pass
    else:
        print("N must be a number")
        exit(1)
    num = int(sys.argv[1])
    if num >= 4:
        global N
        N = num
    else:
        print("N must be at least 4")
        exit(1)
check_argv()
board = [[0]*N for _ in range(N)]


def valid_place(row, col):
    """checks if a queen can be placed without interferance"""
    # check row and col
    for a in range(col):
        if board[row][a] == 1:
            return False
    for b in range(row):
        if board[b][col] == 1:
            return False
    # check diagonals
    for k in range(0, N):
        for l in range(0, N):
            if (k + l == col + row) or (k - l == row - col):
                if board[k][l] == 1:
                    return False
    return True


def solve(queens):
    """Backtrace Method"""
    if queens == 0:
        print(board)
        return True
    for row in range(0, N):
        for col in range(0, N):
            if (valid_place(row, col) is True) and (board[row][col] != 1):
                board[row][col] = 1
                # recursive part
                if solve(queens - 1) is True:
                    return True
                board[row][col] = 0
    return False
solve(N)
