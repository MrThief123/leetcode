'''
377. Combination Sum IV
Use dynamic programming to count the number of combinations that sum up to the target.
Initialize a dp array where dp[i] represents the number of combinations to reach sum i.
Iterate through all sums from 1 to target, and for each sum, iterate through the nums array.
For each number, if it is less than or equal to the current sum, add dp[sum - num] to dp[sum].
'''

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        out = 0
        n = target

        dp = [0 for i in range(target+1)]
        
        for num in nums:
            if num <= target:
                dp[num] = 1

        for i in range(1, n+1):
            for num in nums:
                
                temp = max(i - num, 0)
                dp[i] += dp[temp]

        return dp[-1]
        
