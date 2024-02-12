"""
This program is a minesweeper program and has input as a matrix grid which 
has - where there is no mine and # for where a mine is present. For each 
position where there is no mine it finds out if there is mine adjacent to it 
vertically, horizontally and diagonally. If there is a mine its count is 
increased and total mines adjacent to it is output in the matrix as result
"""


def count_adjacent_mines(matrix_grid, row_current, col_current):
    """
    This function counts the mines adjacent to the mine at current_row and
    current_col.
    param: matrix_grid the whole matrix which has - and #
         : row_current the current row whose adjacent mines are calculated
         : col_current the current col whose adjacent mines are calculated
    return: returns the total mines_found
    """
    row_size = len(matrix_grid)
    col_size = len(matrix_grid[0])
    mines_found = 0

    # Set row_offset to iterate -1, 0 or 1 ie one row before, current row 
    # and next row. Similary set col_offset to -1, 0, 1 to do same for cols
    # Calculate adjacent row, col position by offsetting current row,col
    # with row_offset and col_offset 
    for row_offset in [-1, 0, 1]:
        for col_offset in [-1, 0, 1]:
            row = row_current + row_offset
            col = col_current + col_offset

            # Check for boundary conditions if row or col is 0 or it is last
            # row or col then just continue without checking for # for 
            # previous rows,cols in case of 0 and next rows,cols in case its
            # equal to row_size, col_size
            if row < 0 or row >= row_size or col < 0 or col >= col_size:
               continue
            
            # Check if mine exists if so increase the mines_found count by 1
            if matrix_grid[row][col] == '#':
               mines_found += 1

    return mines_found


def fill_adjacent_counts(mine_grid):
    """
    This function fills the matrix grid whose cells has '-' with count of 
    mines adjacent to it and populates the result_grid with mine counts and
    mines.
    param: mine_grid the matrix having '#' and '-'
    return: result_grid which has the result matrix having '#' and minecount
    """
    row_size = len(mine_grid)      # Declare as length of mine_grid
    col_size = len(mine_grid[0])   # Declare as length of first column
    
    result_grid = mine_grid[:]     # Copy mine_grid to result_grid

    # Loop through the matrix and check if the row is '-' if so call function
    # count_adjacent_mines. Replace the current '-' with total count returned
    # by method
    for row in range(row_size):
        for col in range(col_size):
            if mine_grid[row][col] == '-':
                mines_found = str(count_adjacent_mines(mine_grid, row, col))
                result_grid[row][col] = mines_found
    return result_grid


# Declare the input matrix with - and #
input_grid = [
    ["-", "-", "-", "#", "#"],     
    ["-", "#", "-", "-", "-"],
    ["-", "-", "#", "-", "-"],
    ["-", "#", "#", "-", "-"],
    ["-", "-", "-", "-", "-"]
]

# Call the function to get the matrix with counts of adjacent mines 
output_grid = fill_adjacent_counts(input_grid)

# Print the output_matrix(2D List) returned with - replaced with count of mines 
# adjacent to it in format same as input_grid
print("[ ",end=" ")
for count, cells in enumerate(output_grid, start=0):
    if (count > 0):
        print("   ", end="")
    if (count == len(output_grid) - 1):
        print(cells, end= " ")
    else:
        print(cells)
print(" ]")
    