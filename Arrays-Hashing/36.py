"""
36. Valid Sudoku  [Medium]

Approach:
  - Keep a set per row, column and 3x3 box.
  - On each filled cell, fail if its digit is already in any of its three sets.

Complexity: O(1) time (fixed 9x9 board), O(1) space
"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Initialize sets for rows, columns, and grids
        rows = [set() for i in range(9)]
        columns = [set() for i in range(9)]
        grid = [set() for i in range(9)]

        for i in range(9):
            for j in range(9):
                val = board[i][j]

                if val == '.':
                    continue

                # check row
                if val in rows[i]:
                    return False
                else:
                    rows[i].add(val)

                # check columns
                if val in columns[j]:
                    return False
                else:
                    columns[j].add(val)

                # check grid: boxes are numbered 0-8, left to right, top to bottom
                row = i // 3
                col = j // 3
                pos = row * 3 + col

                if val in grid[pos]:
                    return False
                else:
                    grid[pos].add(val)

        return True
