# Write your solution here
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

#   print(block_correct(sudoku, 0, 0))
  # print(block_correct(sudoku, 1, 2))