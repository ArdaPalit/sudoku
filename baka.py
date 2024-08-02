import numpy as np

sudoku = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

sudoku = np.array(sudoku)

def satir_sutun_cell_check(x, y, z):
    global sudoku
    for i in range(9):
        if sudoku[i][y] == z:
            return False

    for j in range(9):
        if sudoku[x][j] == z:
            return False
    rangeX = (x // 3) * 3
    rangeY = (y // 3) * 3

    for i in range(rangeX, rangeX + 3):
        for j in range(rangeY, rangeY + 3):
            if sudoku[i][j] == z:
                return False
    return True

def empty_spaces():
    global sudoku
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                return i, j
    return False

def solve():
    empty = empty_spaces()
    if not empty:
        return True
    i, j = empty #not mine
    for k in range(1, 10):
        if satir_sutun_cell_check(i, j, k):
            sudoku[i][j] = k
            if solve():
                return True
            sudoku[i][j] = 0
    return False

if solve():
    print(sudoku)
else:
    print("There is no solution of this sudoku...")


