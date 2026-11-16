"""
2352. Equal Row and Column Pairs  [Medium]

Approach (hash rows, probe with columns):
  - Count each row as a tuple in a hash map.
  - Build each column as a tuple and add the number of rows equal to it.

Complexity: O(n^2) time, O(n^2) space
"""

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        from collections import defaultdict
        row_hash = defaultdict(int)  # row tuple -> how many times it appears
        n = len(grid)
        out = 0

        for i in grid:
            row_hash[tuple(i)] += 1

        temp_list = [0 for i in range(n)]  # reused buffer for the current column

        for x in range(n):
            # Build column x
            for y in range(n):
                temp_list[y] = grid[y][x]
            if tuple(temp_list) in row_hash:
                out += row_hash[tuple(temp_list)]
        return out
