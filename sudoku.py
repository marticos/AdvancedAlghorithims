# Sudoku Solver
import time

board = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
         [6, 0, 0, 1, 9, 5, 0, 0, 0],
         [0, 9, 8, 0, 0, 0, 0, 6, 0],
         [8, 0, 0, 0, 6, 0, 0, 0, 3],
         [4, 0, 0, 8, 0, 3, 0, 0, 1],
         [7, 0, 0, 0, 2, 0, 0, 0, 6],
         [0, 6, 0, 0, 0, 0, 2, 8, 0],
         [0, 0, 0, 4, 1, 9, 0, 0, 5],
         [0, 0, 0, 0, 8, 0, 0, 7, 0]]

matteo_s_board = [[3, 2, 0, 0, 0, 0, 7, 0, 8], 
                  [0, 0, 0, 0, 4, 0, 0, 5, 0], 
                  [5, 0, 1, 0, 0, 0, 0, 0, 9], 
                  [0, 0, 0, 9, 0, 0, 0, 0, 0], 
                  [8, 5, 0, 0, 0, 0, 3, 0, 2], 
                  [0, 0, 6, 0, 0, 0, 0, 4, 0], 
                  [0, 0, 0, 0, 0, 0, 1, 0, 0], 
                  [0, 4, 0, 0, 7, 0, 0, 0, 0], 
                  [9, 0, 5, 0, 0, 6, 0, 0, 3]]

wrong_board = [[2,7,0,1,3,6,0,5,9],
               [3,0,0,0,4,0,0,0,1],
               [0,0,9,7,8,5,2,0,0],
               [9,5,0,0,0,0,0,6,4],
               [0,3,0,8,0,9,0,2,0],
               [8,2,0,0,0,0,0,7,3],
               [0,0,2,5,1,8,3,0,0],
               [5,0,0,0,9,0,0,0,2],
               [1,9,0,6,2,7,0,4,8]]


# Problem 1: Print the Sudoku Board

def print_board(board):
  if type(board) != list:
    print("The board is not valid.")
    return
  row_num = 0
  for row in board:
    str_row = ""
    col_num = 0
    for val in row:
      if val == 0:
        val = " "
      else:
        val = str(val)
      if col_num % 3 == 0:
        str_row += "| "
      str_row += val + " "
      col_num += 1
    str_row += "|"
    if row_num % 3 == 0:
      print("-------------------------")
    print(str_row)
    row_num += 1
  print("-------------------------") 


print(board)
print()
print_board(board)
# Make some space
print()

# Problem 2: Find empty cell

def find_zero(board):
  for i in range(len(board)):
    for j in range(len(board[0])):
      if board[i][j] == 0:
        return [i,j]

# print(find_zero(board))

def is_valid(board, row, col, value):
  # Parse the columns to check the row
  for i in range(len(board)): # 0 -> 8
    if board[row][i] == value:
      return False

  # Parse the row to check the column
  for j in range(len(board[0])): # 0 -> 8
    if board[j][col] == value:
      return False
  
  # The 3x3 grids are sub-squares with coordinates 0 to 2
  grid_row = row // 3 # integers 0,1,2
  grid_col = col // 3 # integers 0,1,2
  for x in range(3):
    for y in range(3):
      if board[x + (grid_row * 3)][y + (grid_col * 3)] == value:
        return False

  return True

# print(is_valid(board, 0, 2, 1))
# print(is_valid(board, 0, 2, 7))
# print(is_valid(board, 8, 2, 1))
# print(is_valid(board, 3, 5, 9))

# Problem 4: Solve the Sudoku Problem
times = 0
def solve(board, deep):
  global times
  times += 1
  # print(deep)
  # Base case
  empty_cell = find_zero(board)
  if not empty_cell:
    return board
  
  # Recursive case
  ## Empty cell coordinates
  x = empty_cell[0]
  y = empty_cell[1]
  for i in range(1, 10):
    if is_valid(board, x, y, i):
      board[x][y] = i
      print()
      print_board(board)
      print()
      #time.sleep(0.2)
      print(deep)
      _board = solve(board, deep + 1)
      if _board:
        return _board
      else:
        board[x][y] = 0
  return None

solution = solve(wrong_board, 0)
print(solution)
print()
print_board(solution)
print()
print(times)