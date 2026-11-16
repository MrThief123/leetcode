"""
1304. Find N Unique Integers Sum up to Zero  [Easy]

Approach:
  - Pair each positive integer with its negative: (1, -1), (2, -2), ...
  - If n is odd, add 0 to make up the count.

Complexity: O(n) time, O(n) space
"""

class Solution:
    def sumZero(self, n: int) -> List[int]:
        out = []
        if n % 2 == 0:
            # n/2 cancelling pairs
            for i in range(1, n//2 + 1, 1):
                out.extend([i, -i])
        else:
            # (n-1)/2 pairs plus a zero
            for i in range(1, n//2 + 1, 1):
                out.extend([i, -i])
            out.append(0)
        return out
