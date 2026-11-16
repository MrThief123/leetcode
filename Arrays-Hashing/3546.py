"""
3546. Equal Sum Grid Partition I  [Medium]

Approach (prefix sums):
  - Build prefix sums of row totals and of column totals.
  - A horizontal (or vertical) cut works when the sum before the cut equals the
    sum after it, i.e. prefix[i] == total - prefix[i].

Complexity: O(rows * cols) time, O(rows + cols) space
"""

from typing import List


class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        rows = len(grid)
        cols = len(grid[0])

        prefix_sum_rows = [0 for i in range(rows)]

        prefix_sum_rows[0] = sum(grid[0])

        # compute prefix sums for rows
        for i in range(1, rows):
            prefix_sum_rows[i] = sum(grid[i])
            prefix_sum_rows[i] += prefix_sum_rows[i-1]

        prefix_sum_cols = [0 for i in range(cols)]

        # compute prefix sums for columns
        for i in range(cols):
            for j in range(rows):
                prefix_sum_cols[i] += grid[j][i]

        for i in range(1, cols):
            prefix_sum_cols[i] += prefix_sum_cols[i-1]

        # check for possible splits
        if rows > 1:
            # check horizontal splits (cut after row i)
            for i in range(rows-1):
                if prefix_sum_rows[i] == prefix_sum_rows[-1] - prefix_sum_rows[i]:
                    return True
        # check vertical splits (cut after column i)
        if cols > 1:
            for i in range(cols-1):
                if prefix_sum_cols[i] == prefix_sum_cols[-1] - prefix_sum_cols[i]:
                    return True

        return False
