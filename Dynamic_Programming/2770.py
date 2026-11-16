"""
2770. Maximum Number of Jumps to Reach the Last Index  [Medium]

Approach (forward DP):
  - out[i] = maximum jumps to reach index i, or -1 if unreachable.
  - From a reachable i, you may jump to any j > i with |nums[j] - nums[i]| <= target.
  - Relax every such j with out[i] + 1.

Complexity: O(n^2) time, O(n) space
"""

class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)

        out = [-1 for i in range(n)]  # -1 = unreachable

        out[0] = 0  # we start at index 0

        for i in range(n):
            curr = out[i]
            if curr == -1:
                continue  # can't jump from an unreachable index
            minn = nums[i] - target  # allowed value range for the next index
            maxx = nums[i] + target
            # j is an offset into nums[i+1:], so the real index is j + i + 1
            for j, num in enumerate(nums[i+1:]):
                if minn <= num <= maxx:
                    out[j+i+1] = max(out[j+i+1], curr + 1)
        return out[-1]
