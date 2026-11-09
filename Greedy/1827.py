'''
1827. Minimum Operations to Make the Array Increasing
Iterate through the array while keeping track of the previous element
For each element, if it is less than or equal to the previous element, calculate the required
increments to make it one more than the previous element
Update the previous element to the current element after increments
'''

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        prev = 0

        if n == 1:
            return 0 
        
        for i in nums:
            res += max(0, prev - i + 1)
            prev = max(i, prev + 1)

        return res
        