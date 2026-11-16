"""
1497. Check If Array Pairs Are Divisible by k  [Medium]

Approach (remainder counting):
  - Two numbers sum to a multiple of k iff their remainders sum to k (or both are 0).
  - Count remainders; remainder r must be matched by an equal count of remainder k-r.
  - Remainder 0 pairs with itself, so its count must be even.

Complexity: O(n + k) time, O(k) space
"""

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        from collections import defaultdict

        count = defaultdict(int)  # remainder -> frequency

        # Python's % already returns a non-negative remainder, even for negatives
        for num in arr:
            count[num % k] += 1

        # Case 1: remainder 0 must have even count
        if count[0] % 2 != 0:
            return False

        # Case 2: for each remainder r, count[r] must match count[k-r]
        for r in range(1, k):
            if count[r] != count[k - r]:
                return False

        return True
