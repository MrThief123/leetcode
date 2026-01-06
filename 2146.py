'''
2146. K Highest Ranked Items Within a Price Range
Use a BFS to explore the grid from the starting position
Maintain a max-heap to keep track of the top k items based on distance, price, and coordinates
Expand in all four directions, marking visited cells and adding valid items to the heap
'''

class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        import heapq
        from collections import deque

        rows = len(grid)
        cols = len(grid[0])

        low, high = pricing
        sx, sy = start

        # max-heap for top k items
        max_heap = []

        # BFS queue
        q = deque()
        q.append((sx, sy, 0))

        # visited matrix
        visited = [[False] * cols for _ in range(rows)]
        visited[sx][sy] = True

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while q:
            x, y, dist = q.popleft()

            # If this is a valid item
            if low <= grid[x][y] <= high:
                price = grid[x][y]

                pri = (dist, price, x, y)
                neg_pri = (-dist, -price, -x, -y)

                if len(max_heap) < k:
                    heapq.heappush(max_heap, (neg_pri, pri))
                else:
                    # is the current smaller than kth biggest
                    if neg_pri > max_heap[0][0]:
                        heapq.heapreplace(max_heap, (neg_pri, pri))

            # BFS expansion
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy

                if 0 <= nx < rows and 0 <= ny < cols:
                    if not visited[nx][ny] and grid[nx][ny] != 0:
                        visited[nx][ny] = True
                        q.append((nx, ny, dist + 1))

        # Extract results from heap (sorted by priority)
        result = [pri[2:] for _, pri in sorted(max_heap, key=lambda x: x[1])]

        return result