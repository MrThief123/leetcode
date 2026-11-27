"""
2057. Smallest Index With Equal Value  [Easy]

Approach:
  - Scan left to right and return the first index i where i % 10
    equals nums[i]; the first match found is the smallest.

Complexity: O(n) time, O(1) space
"""

class Solution:
    def smallestEqual(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            if i%10 == nums[i]:
                return i
        return -1
