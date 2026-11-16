"""
238. Product of Array Except Self  [Medium]

Approach (prefix and suffix products):
  - Answer at i = (product of everything left of i) * (product of everything right of i).
  - Example: [1 2 3 4 5 6], without 4 -> (1*2*3) * (5*6) = 180.
  - No division is needed, so zeros are handled naturally.

Complexity: O(n) time; O(n) space (v1) / O(1) extra space (v2)
"""

# Version 1: separate prefix and suffix arrays
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        out = [0 for i in range(n)]

        # prefix_product[i] = product of nums[0..i-1]
        # suffix_product[i] = product of nums[i..n-1]
        prefix_product = [1 for i in range(n + 1)]
        suffix_product = [1 for i in range(n + 1)]

        for i in range(n):
            prefix_product[i+1] = prefix_product[i]*nums[i]
            suffix_product[n-i-1] = suffix_product[n-i]*nums[n-i-1]

        # Left of i times right of i
        for i in range(n):
            out[i] = prefix_product[i]*suffix_product[i+1]

        return out


# Version 2 (optimised): reuse the output array, no extra arrays
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        out = [1] * n

        # prefix pass: out[i] = product of everything left of i
        prefix = 1
        for i in range(n):
            out[i] = prefix
            prefix *= nums[i]

        # suffix pass: multiply in the product of everything right of i
        suffix = 1
        for i in range(n - 1, -1, -1):
            out[i] *= suffix
            suffix *= nums[i]

        return out
