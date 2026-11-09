'''
53. Maximum Subarray
What is the best subarray that ends at the current index? 
Is it 
    the current number, 
    or the current number plus the best subarray that ends at the previous index?
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        out = float('-inf')
        curr = float('-inf')

        for num in nums:
            if num > curr + num:
                curr = num
            else:
                curr = curr + num
            out = max(out, curr)
        
        return out