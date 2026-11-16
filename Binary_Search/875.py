"""
875. Koko Eating Bananas  [Medium]

Approach (binary search on the answer):
  - Speed k works if the total hours sum(ceil(pile / k)) <= h.
  - Feasibility is monotonic in k, so binary search the smallest valid k in [1, max(piles)].

Complexity: O(n log m) time (m = max pile), O(1) space
"""

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        high = max(piles)  # eating the biggest pile each hour always works

        # With exactly one pile per hour we must eat the largest pile in an hour
        if n == h:
            return high

        # Can Koko finish within h hours at speed n?
        def valid(n):
            total = 0
            for i in piles:
                total += (i + n - 1) // n  # ceil(i / n)

            return total <= h

        low = 1

        # Find the smallest valid speed
        while low != high:
            mid = (low+high)//2
            if valid(mid):
                high = mid       # mid works; try slower
            else:
                low = mid + 1    # too slow

        mid = (low+high)//2

        return mid
