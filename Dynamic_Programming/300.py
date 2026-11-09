'''
300. Longest Increasing Subsequence
Use dynamic programming with binary search to efficiently find the length of the longest increasing subsequence.
Maintain a dp array where dp[i] represents the smallest tail of all increasing subsequences of length i+1.
'''

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
