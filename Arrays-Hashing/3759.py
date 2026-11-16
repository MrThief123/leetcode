"""
3759. Count Elements With at Least K Greater Values  [Easy]

Approach:
  - Walk the distinct values from smallest to largest.
  - Value v has at least k larger elements if the n elements not yet removed,
    minus v's own copies, is still >= k.
  - Remove v's copies after counting it, then move to the next value.

Complexity: O(n log n) time, O(n) space
"""

class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        from collections import Counter

        n = len(nums)  # elements not yet processed (current value and larger)
        out = 0

        counts = Counter(nums)

        for key in sorted(counts.keys()):
            # Everything outside key's copies is strictly larger
            if n - counts[key] >= k:
                out += 1
                n -= counts[key]

        return out
