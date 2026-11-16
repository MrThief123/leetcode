"""
724. Find Pivot Index  [Easy]

Approach (prefix sum):
  - Build cumulative sums.
  - At index i, left sum = prefix[i]; right sum = total - prefix[i+1].
  - The first index where they are equal is the pivot.

Complexity: O(n) time, O(n) space
"""

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix_sum = [0 for i in range(len(nums) + 1)]

        for i in range(len(nums)):
            prefix_sum[i+1] = prefix_sum[i] + nums[i]

        for i in range(len(nums)):
            left = prefix_sum[i]                         # sum before i
            right = prefix_sum[-1] - prefix_sum[i+1]     # sum after i
            if left == right:
                return i
        return -1
