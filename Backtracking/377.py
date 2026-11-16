"""
377. Combination Sum IV  [Medium]

(Lives in Backtracking, but it is solved with bottom-up dynamic programming.)

Approach (DP over sums):
  - dp[i] = number of ordered sequences of nums that add up to i.
  - dp[i] = sum of dp[i - num] over each num; the loop over sums on the outside
    makes different orders count separately.
  - Seeding dp[num] = 1 and clamping i - num to 0 lets dp[0] (= 0) contribute
    nothing, so only exact single-number hits are counted by the seed.

Complexity: O(target * len(nums)) time, O(target) space
"""

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        out = 0  # unused
        n = target

        dp = [0 for i in range(target+1)]  # dp[i] = ways to make sum i

        # A single number equal to the sum is one way
        for num in nums:
            if num <= target:
                dp[num] = 1

        for i in range(1, n+1):
            for num in nums:

                temp = max(i - num, 0)  # clamp so we never index below 0
                dp[i] += dp[temp]

        return dp[-1]
