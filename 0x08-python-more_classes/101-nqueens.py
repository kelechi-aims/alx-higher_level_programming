#!/usr/bin/python3
'''
   The N queens puzzle is the challenge of placing
   N non-attacking queens on an N×N chessboard.
   Write a program that solves the N queens problem.
'''


import sys


def is_safe(board, row, col):
    '''
    Checks if a queen can be placed at the given position
    without attacking any other queens on the board.

    Args:
        board (list): The current state of the chessboard.
        row (int): The row index of the position to check.
        col (int): The column index of the position to check.

    Returns:
        bool: True if the position is safe, False otherwise.
    '''
    # Check the current row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check the upper diagonal on the left side
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check the lower diagonal on the left side
    i, j = row, col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve_nqueens(board, col, solutions):
    '''
    Recursive function to solve the N-Queens problem.

    Args:
        board (list): The current state of the chessboard.
        col (int): The current column being considered.
        solutions (list): A list to store the found solutions.

    Return:
        bool: True if a solution is found, False otherwise.
    '''
    # Base case: All queens have been placed
    if col == N:
        queens = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    queens.append([i, j])
        solutions.append(queens)
        return True

    # Recursive case: Try placing a queen in each row of the current column
    for row in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1
            solve_nqueens(board, col + 1, solutions)
            board[row][col] = 0

    return False


def print_solutions(solutions):
    '''
    Prints the solutions to the N-Queens problem.

    Args:
        solutions (list): A list of found solutions.
    '''
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    # Parse the command-line argument
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be an integer")
        sys.exit(1)

    # Create an empty chessboard
    board = [[0 for _ in range(N)] for _ in range(N)]

    # Solve the N-Queens problem
    solutions = []
    solve_nqueens(board, 0, solutions)

    # Print the solutions
    print_solutions(solutions)
