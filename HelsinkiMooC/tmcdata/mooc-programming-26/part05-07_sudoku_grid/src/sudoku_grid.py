# Write your solution here
def sudoku_grid_correct(sudoku: list):
  def row_correct(sudoku: list, row_no: int):
    freq = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}

    for square in sudoku[row_no]:
      if square in freq:
        freq[square] += 1
    print(freq)
  
    for val in freq.values():
      if val > 1:
        return False
    return True
  
  rows = row_correct

  def column_correct(sudoku: list, column_no: int):
    freq = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}

    col = []
    for row in sudoku:
      col.append(row[column_no])

    for num in col:
      if num in freq:
        freq[num] += 1
  
    for val in freq.values():
      if val > 1:
        return False
    return True

  the_columns = column_correct

  def block_correct(sudoku: list, row_no: int, column_no: int):
    the_block = []
    freq = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
  
    for r in range(row_no, row_no + 3):
      this_row = []
      for c in range(column_no, column_no + 3):
        this_row.append(sudoku[r][c])
      the_block.append(this_row)
    print(the_block)

    for row in the_block:
      for num in row:
        if num in freq:
          freq[num] += 1
  
    for val in freq.values():
      if val > 1:
        return False
    return True
  
  the_block = block_correct

  def all_row_correct(sudoku):
    for row_no in range(9):
      if row_correct(sudoku, row_no) == False:
        return False
    return True
  
  def all_columns_correct(sudoko):
    for column_no in range(9):
      if column_correct(sudoku, column_no) == False:
        return False
      return True
  
  def all_blocks_correct(sudoku):
    for row_start in range(0, 9, 3):
      for col_start in range(0, 9, 3):
        if block_correct(sudoku, row_start, col_start) == False:
          return False
    return True

  if the_block(sudoku) == True and the_columns(sudoku) == True and rows(sudoku) == True:
    return True
  return False

  # if __name__ == "__main__":
  #   sudoku = [
  #   [9, 0, 0, 0, 8, 0, 3, 0, 0],
  #   [2, 0, 0, 2, 5, 0, 7, 0, 0],
  #   [0, 2, 0, 3, 0, 0, 0, 0, 4],
  #   [2, 9, 4, 0, 0, 0, 0, 0, 0],
  #   [0, 0, 0, 7, 3, 0, 5, 6, 0],
  #   [7, 0, 5, 0, 6, 0, 4, 0, 0],
  #   [0, 0, 7, 8, 0, 3, 9, 0, 0],
  #   [0, 0, 1, 0, 0, 0, 0, 0, 3],
  #   [3, 0, 0, 0, 0, 0, 0, 0, 2]
  # ]

  # print(sudoku_grid_correct(sudoku))
  # print(sudoku_grid_correct(sudoku))