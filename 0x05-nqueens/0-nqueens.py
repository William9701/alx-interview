import sys
from typing import List


def print_solution(board: List[List[int]]) -> None:
    """
    Prints the solution of the N queens problem.

    Args:
        board (List[List[int]]): The chessboard represented as a 2D list.
    """
    solution = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                solution.append([i, j])
    print(solution)


def is_safe(board: List[List[int]], row: int, col: int) -> bool:
    """
    Checks if a queen can be placed at board[row][col].

    Args:
        board (List[List[int]]): The chessboard represented as a 2D list.
        row (int): The row index.
        col (int): The column index.

    Returns:
        bool: True if safe, False otherwise.
    """
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def solve_n_queens(board: List[List[int]], col: int) -> bool:
    """
    Solves the N queens problem using backtracking.

    Args:
        board (List[List[int]]): The chessboard represented as a 2D list.
        col (int): The column index.

    Returns:
        bool: True if solution exists, False otherwise.
    """
    if col == len(board):
        print_solution(board)
        return True
    res = False
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            res = solve_n_queens(board, col + 1) or res
            board[i][col] = 0
    return res


def solve(N: int) -> None:
    """
    Solves the N queens problem.

    Args:
        N (int): The number of queens and the size of the chessboard.
    """
    board = [[0] * N for _ in range(N)]
    if not solve_n_queens(board, 0):
        print("Solution does not exist")
        return


def main() -> None:
    """
    The main function that checks the command line arguments and calls the solve function.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    solve(N)


if __name__ == "__main__":
    main()
