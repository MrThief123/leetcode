"""
3560. Minimum Cost to Cut a Log  [Medium]

Approach (direct formula):
  - Two logs of lengths n and m must each be cut into pieces of length <= k
    (the constraints guarantee each needs at most one cut).
  - Cutting a log of length L > k into pieces k and L - k costs k * (L - k).
  - Sum that cost for each log that is longer than k.

Complexity: O(1) time, O(1) space
"""

class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        out = 0

        # Log n is too long: cut it into k and n - k
        if n > k:
            out += k * (n-k)
        # Log m is too long: cut it into k and m - k
        if m > k:
            out += k * (m-k)
        return out
