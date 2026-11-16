"""
2395. Find Subarrays With Equal Sum  [Easy]

Approach:
  - Compute the sum of every adjacent pair; if a sum repeats, return True.

Complexity: O(n) time, O(n) space
"""

class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        sums = {}  # pair sums seen so far

        for i in range(len(nums) - 1):
            j = i + 1

            total = nums[i] + nums[j]

            if total in sums:
                return True
            else:
                sums[total] = True
        return False
