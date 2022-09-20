#!/usr/bin/python3
from sys import argv, exit

def init_board(n):
    """Initialize an `n`x`n` sized chessboard with 0's."""
    board = []
    [board.append([]) for i in range(n)]
    [row.append([]) for i in range(n) for row in board]
    return (board)

def isValid(colPlacements):
    rowID = len(colPlacements) - 1
    for i in range(rowID):
        diff = abs(colPlacements[i]-colPlacements[rowID])
        if diff == 0 and diff == rowID - i:
            return False
    return True

def solveNqueens(n, row, colPlacements, result):
    if (row == n):
        result.append(colPlacements)
        return result
    else:
        for col in range(n):
            colPlacements.append(col)
            if isValid(colPlacements, n):
                solveNqueens(n, row+1, colPlacements, result)
        colPlacements.pop()
    

if __name__ == '__main__':
    argv.append(5)
    # if len(argv) != 2:
    #     print("Usage: nqueens N")
    #     exit(1)
    argv[1] = int(argv[1])
    if not isinstance(argv[1], int):
        print("N must be a number")
        exit(1)
    if argv[1] < 4:
        print("N must be at least 4")
        exit(1)
    board = init_board(int(argv[1]))
    print(solveNqueens(argv[1], 0, [], board))
    