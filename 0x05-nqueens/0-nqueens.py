#!/usr/bin/python3
""" A program that solves the N queens problem
"""
import sys
from typing import List, Tuple


def print_solution(solution: List[Tuple[int, int]]) -> None:
    """
    Print the N-queens solution in the specified format.

    Parameters:
        solution (List[Tuple[int, int]]): List of queen positions.
    """
    for row, col in solution:
        print(f'[{row}, {col}]', end=' ')
    print()


def is_safe(board: List[Tuple[int, int]], row: int, col: int) -> bool:
    """
    Check if placing a queen at a specific position is safe.

    Parameters:
        board (List[Tuple[int, int]]): List of queen positions.
        row (int): The current row to check.
        col (int): The current column to check.

    Returns:
        bool: True if placing a queen is safe, False otherwise.
    """
    for prev_row, prev_col in board:
        if col == prev_col or row - col == prev_row - prev_col or row + col == prev_row + prev_col:
            return False
    return True


def solve_nqueens(n: int, board: List[Tuple[int, int]], row: int,
                  solutions: List[List[Tuple[int, int]]]) -> None:
    """
    Recursively solve the N-queens problem and store solutions.

    Parameters:
        n (int): Size of the chessboard.
        board (List[Tuple[int, int]]): List of queen positions.
        row (int): Current row being processed.
        solutions (List[List[Tuple[int, int]]]): List to store solutions.
    """
    if row == n:
        solutions.append(board.copy())
        return

    for col in range(n):
        if is_safe(board, row, col):
            board.append((row, col))
            solve_nqueens(n, board, row + 1, solutions)
            board.pop()


def nqueens(N: str) -> None:
    """
    Main function to solve the N-queens problem.

    Parameters:
        N (str): The size of the chessboard passed as a string.

    Prints:
        All possible solutions to the N-queens problem.
    """
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)

    N = int(N)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions: List[List[Tuple[int, int]]] = []
    solve_nqueens(N, [], 0, solutions)

    for solution in solutions:
        print_solution(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    nqueens(sys.argv[1])
