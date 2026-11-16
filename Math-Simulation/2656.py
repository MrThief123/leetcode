"""
2656. Maximum Sum With Exactly K Elements  [Easy]

Approach (greedy):
  - Always pick the current maximum and replace it with max + 1.
  - So the picks are best, best+1, ..., best+k-1.

Complexity: O(k) time, O(1) space (the closed form k*best + k*(k-1)/2 is O(1))
"""

class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        best = max(nums)  # start from the largest element
        out = 0
        for i in range(0, k):
            out += best + i  # the i-th pick is best + i

        return out
