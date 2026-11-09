'''
House Robber Problem - Find the maximum amount of money that can be robbed without robbing two adjacent houses
Use dynamic programming to keep track of the maximum amount that can be robbed up to each house
For each house, decide whether to 
    rob it (and add its value to the maximum from two houses ago) or 
    skip it (and take the maximum from the previous house)
    
Return the maximum amount that can be robbed from all houses
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)

        if n <= 2:
            return max(nums)


        sol = [0 for i in range(n)]

        sol[0] = nums[0]
        sol[1] = max(nums[0], nums[1])

        for i in range(2,  n):
            sol[i] = max(sol[i-2] + nums[i], sol[i-1])
        
        return sol[-1]

        