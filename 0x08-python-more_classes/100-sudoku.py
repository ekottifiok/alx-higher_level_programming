board = []

if col == board[row].length:
    

for i in range(10):
    board[row][col] = i
    if validPlacement(row, col):
        if solve(row, col+1, board):
            return True
        
board[row][col] = []