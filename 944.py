'''
944. Rotting Oranges
Use BFS to simulate the rotting process of oranges over time.
'''

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        rows = len(grid)
        columns = len(grid[0])
        queue = deque()
        fresh = 0
        seen = set()

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for i in range(rows):
            for j in range(columns):
                curr = (i, j)
                if grid[i][j] == 2:
                    seen.add(curr)
                    queue.append(curr)
                elif grid[i][j] == 1:
                    fresh += 1
        
        if fresh == 0:
            return 0

        minutes = 0

        while queue:
            minutes += 1

            # mutli source bfs
            for _ in range(len(queue)):
                x, y = queue.popleft()

                for nx, ny in directions:
                    nx = x + nx
                    ny = y + ny

                    if 0 <= nx < rows and 0 <= ny < columns and grid[nx][ny] == 1 and (nx, ny) not in seen:
                        seen.add((nx, ny))
                        queue.append((nx, ny))
                        fresh -= 1

        if fresh <= 0:
            return minutes - 1
        return -1