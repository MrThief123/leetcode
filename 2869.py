'''
2869. Use hasp map to store seen numbers
Iterate through K, 0 
'''

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        used = [False for i in range(k+1)]
        out = 0
        temp = k

        for i in range(len(nums)-1, -1, -1):
            if nums[i] <= k and used[nums[i]] == False:
                used[nums[i]] = True
                temp -= 1
            out += 1

            if temp == 0:
                return out