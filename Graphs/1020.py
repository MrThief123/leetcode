'''
1020. Number of Enclaves
Use DFS to mark all land cells connected to the boundary as 0
Count the remaining land cells 1 in the grid after the DFS traversal
'''

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        rows = len(grid)
        columns = len(grid[0])

        def dfs(row, column):
            grid[row][column] = 0

            for d in directions:
                x = row + d[0]
                y = column + d[1]

                if 0 <= x < rows and 0 <= y < columns and grid[x][y] == 1:
                    dfs(x, y)

        for i in range(columns):
            if grid[0][i] == 1:
                dfs(0, i)
            if grid[rows - 1][i] == 1:
                dfs(rows - 1, i)

        for j in range(rows):
            if grid[j][0] == 1:
                dfs(j, 0)
            if grid[j][columns - 1] == 1:
                dfs(j, columns - 1)

        return sum(sum(row) for row in grid)