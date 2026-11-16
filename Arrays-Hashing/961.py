"""
961. N-Repeated Element in Size 2N Array  [Easy]

Approach:
  - Exactly one value repeats, so the first value seen twice is the answer.

Complexity: O(n) time, O(n) space
"""

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        seen = set()

        for num in nums:
            if num in seen:
                return num
            seen.add(num)
