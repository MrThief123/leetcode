"""
3531. Count Covered Buildings  [Medium]

Approach:
  - Group building coordinates by row and by column.
  - A building is covered if its row has buildings on both left and right
    and its column has buildings both above and below.
  - Only the min and max of each group are needed, so sort and check the ends.

Complexity: O(m log m) time (m = buildings), O(m) space
"""

class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        from collections import defaultdict

        rows = defaultdict(list)  # row -> columns occupied
        cols = defaultdict(list)  # column -> rows occupied

        # Group buildings by row and column
        for r, c in buildings:
            rows[r].append(c)
            cols[c].append(r)

        # Sort each row and column list
        for r in rows:
            rows[r].sort()
        for c in cols:
            cols[c].sort()

        covered = 0

        # Check each building
        for r, c in buildings:
            row_list = rows[r]
            col_list = cols[c]

            # left = exists column < c
            # right = exists column > c
            has_left = row_list[0] < c
            has_right = row_list[-1] > c

            # above = exists row < r
            # below = exists row > r
            has_above = col_list[0] < r
            has_below = col_list[-1] > r

            if has_left and has_right and has_above and has_below:
                covered += 1

        return covered
