'''
Use DP array to store the best (max) result for each index
'''

class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)

        out = [-1 for i in range(n)]

        out[0] = 0

        for i in range(n):
            curr = out[i]
            if curr == -1:
                continue
            minn = nums[i] - target
            maxx = nums[i] + target
            for j, num in enumerate(nums[i+1:]):
                if minn <= num <= maxx:
                    out[j+i+1] = max(out[j+i+1], curr + 1)
        return out[-1]