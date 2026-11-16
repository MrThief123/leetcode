"""
300. Longest Increasing Subsequence  [Medium]

Approach (patience sorting / tails array):
  - dp[i] holds the smallest possible tail of any increasing subsequence of length i+1.
  - For each num, binary search the first tail >= num:
      * past the end -> extend the LIS
      * otherwise -> replace that tail with the smaller num (improves future options)
  - The LIS length is len(dp). (dp itself is not necessarily a valid subsequence.)

Complexity: O(n log n) time, O(n) space
"""

from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []  # dp[i] = smallest ending value of an increasing subsequence of length i+1

        for num in nums:
            idx = bisect_left(dp, num)
            if idx == len(dp):
                dp.append(num)     # extend LIS
            else:
                dp[idx] = num      # improve tail

        return len(dp)
