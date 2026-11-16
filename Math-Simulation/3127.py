"""
3127. Make a Square with the Same Color  [Easy]

Approach:
  - Map B -> +1 and W -> -1 and check every 2x2 block.
  - A block sums to +/-4 (all same) or +/-2 (three same, one different), and in
    both cases at most one flip makes it uniform.
  - A sum of 0 means a 2-2 split, which would need two flips.

Complexity: O(rows * cols) time, O(1) space
"""

from typing import List


class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        c = {'B': 1,
            'W': -1}

        n = len(grid)
        m = len(grid[0])

        if n < 2 or m < 2:
            return False

        # (i, j) is the top-left corner of each 2x2 block
        for i in range(n-1):
            for j in range(m-1):
                temp = c[grid[i][j]] + c[grid[i+1][j]] + c[grid[i][j+1]] + c[grid[i+1][j+1]]

                if abs(temp) in [2, 4]:
                    return True
        return False
