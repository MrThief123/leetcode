"""
53. Maximum Subarray  [Medium]

Approach (Kadane's algorithm):
  - Best subarray ending at the current index is either
      * the current number alone, or
      * the current number plus the best subarray ending at the previous index.
  - The answer is the best value seen over all indices.

Complexity: O(n) time, O(1) space
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        out = float('-inf')   # best overall
        curr = float('-inf')  # best ending at this index

        for num in nums:
            if num > curr + num:
                curr = num         # starting fresh beats extending
            else:
                curr = curr + num  # extend the previous subarray
            out = max(out, curr)

        return out
