'''
3341. Minimum Time to Reach Target Cell in a Grid
Use Dijkstra's algorithm to find the minimum time to reach the bottom-right cell
Account for the time constraints of each cell when moving
'''

from ast import List


class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        import heapq
        rows, cols = len(moveTime), len(moveTime[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        dp = [[float('inf')] * cols for _ in range(rows)]
        dp[0][0] = 0

        heap = [(0, 0, 0)]

        while heap:
            time, x, y = heapq.heappop(heap)
        
            # If we have already found a better time, skip
            if time > dp[x][y]:
                continue

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                # Check bounds
                if 0 <= nx < rows and 0 <= ny < cols:
                    # Earliest time we can move
                    next_time = max(time+1, moveTime[nx][ny] + 1)

                    # Update dp and push to heap if we found a better time
                    if next_time < dp[nx][ny]:
                        heapq.heappush(heap, (next_time, nx, ny))
                        dp[nx][ny] = next_time

        return dp[rows-1][cols-1]
