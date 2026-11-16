"""
2078. Two Furthest Houses With Different Colors  [Easy]

Approach (single pass):
  - Track p = first index whose color differs from colors[0].
  - A house differing from colors[0] pairs with index 0 (distance i).
  - A house matching colors[0] pairs with the earliest differing house p (distance i - p).

Complexity: O(n) time, O(1) space
"""

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        p, res = inf, 0  # p: first differing index, res: best distance so far
        for i, c in enumerate(colors):
            if (c != colors[0]):
                # Differs from the first house, so distance to index 0 is i
                res = i
                p = min(p, i)
            else:
                # Same as the first house, pair with the earliest differing one
                res = max(res, i - p)
        return res
