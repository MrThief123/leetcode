"""
2150. Find All Lonely Numbers in the Array  [Medium]

Approach:
  - Count every number.
  - A number is lonely if it appears once and neither num-1 nor num+1 exists.

Complexity: O(n) time, O(n) space
"""

class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        from collections import Counter

        counts = Counter(nums)
        out = []

        for num in nums:
            if num+1 not in counts and num-1 not in counts and counts[num] == 1:
                out.append(num)

        return out
