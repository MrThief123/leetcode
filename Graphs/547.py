"""
547. Number of Provinces  [Medium]

Approach (DFS over connected components):
  - Start a DFS from every unvisited city; it marks the whole province.
  - The number of DFS starts equals the number of provinces.

NOTE: `out = 1` should be `out += 1`; as written it can only ever return 0 or 1.
      Left unchanged.

Complexity: O(n^2) time, O(n) space
"""

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        out = 0  # provinces counted

        def dfs(city):
            visited.add(city)
            for i, connected in enumerate(isConnected[city]):
                if connected and i not in visited:
                    dfs(i)

        for i in range(len(isConnected)):
            if i not in visited:
                dfs(i)       # explores one whole province
                out = 1      # BUG: should be `out += 1` (see NOTE)

        return out
