'''
200. Number of Islands
Use BFS to explore and mark all connected land cells for each unvisited land cell
Count the number of BFS initiations to get the total number of islands
'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = [[False] * cols for _ in range(rows)]

        out = 0

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        # BFS function to explore the island
        def bfs(x, y):
            visited[x][y] = True

            for d in directions:
                nx = x + d[0]
                ny = y + d[1]

                # Check bounds and if the cell is land and unvisited
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == '1' and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    bfs(nx, ny)
        
        # Main loop to find islands
        for i in range(rows):
            for j in range(cols):
                # If we find an unvisited land cell, it's a new island
                if grid[i][j] == '1' and visited[i][j] == False:
                    bfs(i, j)
                    out += 1

        return out
