'''
2577. Minimum Time to Visit a Cell in a Grid
Use Dijkstra's algorithm to find the minimum time to reach the bottom-right cell
Account for the time constraints of each cell and parity conditions when moving
'''

class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        import heapq

        rows = len(grid)
        cols = len(grid[0])

        # Early impossible check, if both right and down from start are > 1
        if rows > 1 and cols > 1 and grid[0][1] > 1 and grid[1][0] > 1:
            return -1

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # dp[r][c] = minimum time to reach cell (r, c)
        dp = [[float('inf')] * cols for _ in range(rows)]
        dp[0][0] = 0

        # Min-heap: (time, x, y)
        heap = [(0, 0, 0)]

        # Dijkstra's algorithm
        # use a priority queue to always expand the least time cell
        while heap:
            time, x, y = heapq.heappop(heap)

            if (x, y) == (rows - 1, cols - 1):
                return time

            # If we have already found a better time, skip
            if time > dp[x][y]:
                continue

            for dx, dy in directions:
                nx = x + dx
                ny = y + dy

                if 0 <= nx < rows and 0 <= ny < cols:
                    # Earliest time we can move
                    next_time = max(time + 1, grid[nx][ny])

                    # Parity adjustment
                    # if the difference in time is even, we need to wait an extra unit
                    if (next_time - time) % 2 == 0:
                        next_time += 1

                    # Update dp and push to heap if we found a better time
                    if next_time < dp[nx][ny]:
                        dp[nx][ny] = next_time
                        heapq.heappush(heap, (next_time, nx, ny))
        return -1