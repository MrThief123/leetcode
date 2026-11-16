"""
787. Cheapest Flights Within K Stops  [Medium]

Approach (level-by-level BFS with a best-cost table):
  - BFS by number of stops, so each queue entry is (stops, city, cost so far).
  - Only enqueue a neighbour when it improves the best known cost to that city.
  - Stop expanding paths that have used more than k stops.

Complexity: O(E * k) worst case time, O(V + E) space
"""

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        from collections import defaultdict, deque

        # Adjacency list: city -> [(neighbour, price)]
        graph = defaultdict(list)
        for start, neighbour, price in flights:
            graph[start].append((neighbour, price))

        dp = [float('inf')] * n  # cheapest known cost to each city
        dp[src] = 0

        # BFS queue (stops, node, cost)
        # note: no need for priority queue since each step is + 1 and get appended to the end
        queue = deque([(0, src, 0)])

        while queue:
            stops, node, cost = queue.popleft()

            # Too many stops used
            if stops > k:
                continue

            for neighbour, price in graph[node]:
                new_cost = cost + price
                new_stops = stops + 1

                # Only continue along cheaper routes
                if new_cost < dp[neighbour]:
                    dp[neighbour] = new_cost
                    queue.append((new_stops, neighbour, new_cost))

        return dp[dst] if dp[dst] != float('inf') else -1
