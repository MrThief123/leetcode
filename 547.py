'''
Find the number of connected components (provinces) in an undirected graph
Use Depth-First Search (DFS) to explore all connected nodes from each unvisited node
Keep track of visited nodes to avoid counting the same component multiple times
Increment the province count each time a new unvisited node is found
'''

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        out = 0

        def dfs(city):
            visited.add(city)
            for i, connected in enumerate(isConnected[city]):
                if connected and i not in visited:
                    dfs(i)

        for i in range(len(isConnected)):
            if i not in visited:
                dfs(i)
                out = 1

        return out