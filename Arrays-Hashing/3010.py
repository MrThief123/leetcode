"""
3010. Divide an Array Into Subarrays With Minimum Cost I  [Easy]

Approach:
  - The first subarray always starts at nums[0], so its cost is fixed.
  - The other two subarrays start at any two later positions, so pick the two
    smallest remaining values.

Complexity: O(n) time, O(1) space
"""

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        cost = nums[0]  # forced first cost

        min1, min2 = float('inf'), float('inf')  # two smallest after index 0

        for num in nums[1:]:
            if num <= min1:
                min2 = min1
                min1 = num
            elif num <= min2:
                min2 = num

        return cost + min1 + min2
