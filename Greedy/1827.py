"""
1827. Minimum Operations to Make the Array Increasing  [Easy]

Approach (greedy):
  - Each element must be at least (previous final value + 1).
  - If it is smaller, raise it by the shortfall and add that to the answer.
  - `prev` tracks the final (possibly raised) value of the previous element.

Complexity: O(n) time, O(1) space
"""

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0   # total increments
        prev = 0  # final value of the previous element

        if n == 1:
            return 0

        for i in nums:
            res += max(0, prev - i + 1)  # raise i to prev + 1 if needed
            prev = max(i, prev + 1)      # the value i ends up as

        return res
