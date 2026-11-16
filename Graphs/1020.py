"""
1020. Number of Enclaves  [Medium]

Approach (flood from the border):
  - Land connected to the boundary can walk off the grid, so DFS from every
    border land cell and sink it (set to 0).
  - Whatever land remains is enclosed; the answer is the count of remaining 1s.

Complexity: O(rows * cols) time, O(rows * cols) space (recursion)
"""

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        rows = len(grid)
        columns = len(grid[0])

        # Sink all land connected to (row, column)
        def dfs(row, column):
            grid[row][column] = 0

            for d in directions:
                x = row + d[0]
                y = column + d[1]

                if 0 <= x < rows and 0 <= y < columns and grid[x][y] == 1:
                    dfs(x, y)

        # Top and bottom borders
        for i in range(columns):
            if grid[0][i] == 1:
                dfs(0, i)
            if grid[rows - 1][i] == 1:
                dfs(rows - 1, i)

        # Left and right borders
        for j in range(rows):
            if grid[j][0] == 1:
                dfs(j, 0)
            if grid[j][columns - 1] == 1:
                dfs(j, columns - 1)

        # Count remaining (enclosed) land cells
        return sum(sum(row) for row in grid)
