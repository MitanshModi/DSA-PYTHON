# Function to check if placing a number at grid[row][col] is valid
def is_valid(board, row, col, num):
    # Check if the number is already present in the current row
    for x in range(9):
        if board[row][x] == num:
            return False

    # Check if the number is already present in the current column
    for x in range(9):
        if board[x][col] == num:
            return False

    # Check if the number is already present in the current 3x3 subgrid
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False

    return True


# Function to solve the Sudoku board using backtracking
def solve_sudoku(board):
    # Find an empty cell (represented by 0)
    empty_cell = find_empty(board)
    if not empty_cell:
        return True  # Puzzle solved

    row, col = empty_cell

    # Try numbers from 1 to 9
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            # Place the number
            board[row][col] = num

            # Recursively try to solve with the new number
            if solve_sudoku(board):
                return True

            # Backtrack: Reset the cell if placing num didn't lead to a solution
            board[row][col] = 0

    return False  # Trigger backtracking if no number is valid


# Function to find the next empty cell (represented by 0)
def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)  # Return the row and column index of the empty cell
    return None


# Function to print the Sudoku board in a readable format
def print_board(board):
    for row in board:
        print(" ".join(str(num) for num in row))


# Sample Sudoku puzzle (0 represents empty cells)
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("Sudoku Puzzle:")
print_board(board)

# Solve the Sudoku puzzle
if solve_sudoku(board):
    print("\nSolved Sudoku Puzzle:")
    print_board(board)
else:
    print("No solution exists")
