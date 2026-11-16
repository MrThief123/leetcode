"""
1679. Max Number of K-Sum Pairs  [Medium]

Approach (count complements):
  - Count each number.
  - For each key, its partner is k - key.
      * Partner equals key: pairs among itself = count // 2.
      * Otherwise: min(count[key], count[partner]) pairs, then zero both so the
        pair isn't counted again from the other side.

Complexity: O(n) time, O(n) space
"""

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        from collections import Counter

        counts = Counter(nums)

        out = 0

        for key, value in counts.items():
            rem = k - key  # the number that pairs with key

            if rem == key:
                out += value//2
            elif rem in counts:
                out += min(value, counts[rem])
                # Mark both as used so the mirrored visit adds nothing
                counts[key] = 0
                counts[rem] = 0

        return out
