'''
Use prefix and suffix products to calculate the product of all elements except the current one
[1 2 3 4 5 6]
Product withot 4 = [1 * 2 * 3] * [5 * 6] = 180
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        out = [0 for i in range(n)]
        
        prefix_product = [1 for i in range(n + 1)]
        suffix_product = [1 for i in range(n + 1)]

        for i in range(n):
            prefix_product[i+1] = prefix_product[i]*nums[i]
            suffix_product[n-i-1] = suffix_product[n-i]*nums[n-i-1]
        
        
        for i in range(n):
            out[i] = prefix_product[i]*suffix_product[i+1]

        return out
    
# Optimised version without extra space
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        out = [1] * n

        # prefix pass
        prefix = 1
        for i in range(n):
            out[i] = prefix
            prefix *= nums[i]

        # suffix pass
        suffix = 1
        for i in range(n - 1, -1, -1):
            out[i] *= suffix
            suffix *= nums[i]

        return out
