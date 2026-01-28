'''
3423. Maximum Adjacent Distance
You are given a 0-indexed integer array nums. The adjacent distance of two adjacent integers in nums is defined as the absolute difference between them.
Return the maximum adjacent distance of nums after you insert the last element of nums at the beginning of nums and the first element of nums at the end of nums.
'''

class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        nums = [nums[-1]] + nums + [nums[0]]
        
        out = 0

        for i in range(len(nums)-1):
            out = max(out, abs(nums[i] - nums[i+1]))

        return out