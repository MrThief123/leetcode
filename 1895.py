'''
1895. Largest Magic Square
Use prefix sums to efficiently calculate sums of rows and columns,
and check for magic square properties.
'''

from ast import List


class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        
        # Compute prefix sums for rows and columns
        prefix_rows = [[0] * (columns + 1) for _ in range(rows)]
        prefix_cols = [[0] * (rows + 1) for _ in range(columns)]
        
        # Fill prefix sum arrays
        for i in range(rows):
            for j in range(columns):
                val = grid[i][j]
                prefix_rows[i][j+1] = prefix_rows[i][j] + val
                prefix_cols[j][i+1] = prefix_cols[j][i] + val

        # Iterate over possible square sizes from largest to smallest
        for l in range(min(rows, columns), 1, -1):
            for row in range(0, rows - l + 1):
                for col in range(0, columns - l + 1):

                    # target sum = first row
                    target = prefix_rows[row][col + l] - prefix_rows[row][col]

                    # check all rows
                    ok = True
                    for r in range(row, row + l):
                        if prefix_rows[r][col + l] - prefix_rows[r][col] != target:
                            ok = False
                            break
                    if not ok:
                        continue

                    # check all columns
                    for c in range(col, col + l):
                        if prefix_cols[c][row + l] - prefix_cols[c][row] != target:
                            ok = False
                            break
                    if not ok:
                        continue

                    up_dig = 0
                    down_dig = 0

                    for i in range(l):
                        up_dig += grid[row + i][col + i]              # main diagonal
                        down_dig += grid[row + i][col + l - 1 - i]    # anti-diagonal 

                    if up_dig == target and down_dig == target:
                        return l

        return 1