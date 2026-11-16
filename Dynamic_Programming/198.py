"""
198. House Robber  [Medium]

Approach (1D DP):
  - sol[i] = best loot using houses 0..i with no two adjacent.
  - For house i: rob it (nums[i] + sol[i-2]) or skip it (sol[i-1]); take the better.

Complexity: O(n) time, O(n) space (O(1) with two rolling variables)
"""

class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)

        # With one or two houses just take the largest
        if n <= 2:
            return max(nums)

        sol = [0 for i in range(n)]

        # Base cases
        sol[0] = nums[0]
        sol[1] = max(nums[0], nums[1])

        for i in range(2, n):
            sol[i] = max(sol[i-2] + nums[i], sol[i-1])

        return sol[-1]
