#!/usr/bin/python3
"""Solve the famous N Queen Problem"""
import sys


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)


def print_error(message):
    """Print the error message and exit with status 1"""
    print(message)
    sys.exit(1)


try:
    n = int(sys.argv[1])
except ValueError:
    print_error("N must be a number")

if n < 4:
    print_error("N must be at least 4")

col = set()
# (r - c)
positive_diagonal = set()
# (r + c)
negative_diagonal = set()
# The original board
board = []


def backtracking(r):
    """Backtracking function"""
    if r == n:
        print(board)
        return
    for c in range(n):
        if c in col or (r - c) in positive_diagonal or \
                (r + c) in negative_diagonal:
            continue

        col.add(c)
        positive_diagonal.add(r - c)
        negative_diagonal.add(r + c)

        board.append([r, c])

        backtracking(r + 1)

        col.remove(c)
        positive_diagonal.remove(r - c)
        negative_diagonal.remove(r + c)
        board.pop()


backtracking(0)