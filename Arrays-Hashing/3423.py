"""
3423. Maximum Difference Between Adjacent Elements in a Circular Array  [Easy]

Approach:
  - Circular adjacency just adds the pair (last, first).
  - Pad the array with the last element in front and the first element behind,
    then take the max absolute difference of neighbours.

Complexity: O(n) time, O(n) space
"""

class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        nums = [nums[-1]] + nums + [nums[0]]  # wrap around both ends

        out = 0

        for i in range(len(nums)-1):
            out = max(out, abs(nums[i] - nums[i+1]))

        return out
