"""
3512. Minimum Operations to Make Array Sum Divisible by K  [Easy]

Approach:
  - Each operation decrements one element by 1, so it lowers the sum by 1.
  - Reaching a multiple of k takes exactly (sum % k) operations.

Complexity: O(n) time, O(1) space
"""

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return sum(nums) % k
