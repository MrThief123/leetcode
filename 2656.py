'''
2656. Maximum Sum With Exactly K Elements
Select the largest element from the array and add it k times, incrementing it by 1
'''

class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        best = max(nums)
        out = 0
        for i in range(0, k):
            out += best + i

        return out