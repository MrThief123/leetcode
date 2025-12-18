'''
Determine if it's possible to jump to the last index of the array
Use a greedy approach to track the furthest reachable index
Iterate backwards through the array, updating the goal index when a position can reach it
Return true if the starting index can reach the goal index, otherwise false
'''

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        
        return True if goal == 0 else False