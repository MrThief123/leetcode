"""
3341. Minimum Time to Reach Room I  [Medium]

Approach (Dijkstra):
  - moveTime[r][c] is the earliest moment we may start moving into that room;
    each move then takes 1 second.
  - Arrival time at a neighbour = max(current time, moveTime[neighbour]) + 1.
  - Always expand the room with the smallest arrival time.

Complexity: O(rows * cols * log(rows * cols)) time, O(rows * cols) space
"""

from ast import List


class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        import heapq
        rows, cols = len(moveTime), len(moveTime[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        # dp[r][c] = earliest arrival time at (r, c)
        dp = [[float('inf')] * cols for _ in range(rows)]
        dp[0][0] = 0

        heap = [(0, 0, 0)]  # (time, row, col)

        while heap:
            time, x, y = heapq.heappop(heap)

            # If we have already found a better time, skip
            if time > dp[x][y]:
                continue

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                # Check bounds
                if 0 <= nx < rows and 0 <= ny < cols:
                    # Earliest time we can move: wait for the room to open, then 1s to move
                    next_time = max(time+1, moveTime[nx][ny] + 1)

                    # Update dp and push to heap if we found a better time
                    if next_time < dp[nx][ny]:
                        heapq.heappush(heap, (next_time, nx, ny))
                        dp[nx][ny] = next_time

        return dp[rows-1][cols-1]
