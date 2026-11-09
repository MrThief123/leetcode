'''
787. Cheapest Flights Within K Stops
Use a modified BFS to explore all flight paths up to K stops
Maintain a cost array to track the minimum cost to reach each city
Update the cost array and queue when a cheaper path to a city is found within the allowed stops
'''

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        from collections import defaultdict, deque

        graph = defaultdict(list)
        for start, neighbour, price in flights:
            graph[start].append((neighbour, price))

        dp = [float('inf')] * n
        dp[src] = 0

        # BFS queue (stops, node, cost)
        # note: no need for priority queue since each step is + 1 and get appended to the end
        queue = deque([(0, src, 0)])

        while queue:
            stops, node, cost = queue.popleft()

            if stops > k:
                continue

            for neighbour, price in graph[node]:
                new_cost = cost + price
                new_stops = stops + 1

                if new_cost < dp[neighbour]:
                    dp[neighbour] = new_cost
                    queue.append((new_stops, neighbour, new_cost))

        return dp[dst] if dp[dst] != float('inf') else -1
