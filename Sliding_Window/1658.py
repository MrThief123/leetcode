'''
1658. Minimum Operations to Reduce X to Zero
Medium
Use prefix sums from both ends to find combinations that sum to x.
'''

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:        
        prefix_left = {}
        prefix_right = {}
        n = len(nums)

        prefix_left[0] = 0
        prefix_right[0] = n+1

        sum_left = 0
        sum_right = 0

        out = pow(10,6)

        for i, num in enumerate(nums):
            sum_left += num
            prefix_left[sum_left] = i+1

            sum_right += nums[n-i-1]
            prefix_right[sum_right] = n-i


        for i, left in prefix_left.items():
            diff = x - i

            if diff in prefix_right:
                
                right = prefix_right[diff]

                if left < right:
                    out = min(out, left + n - right+1)
                else:
                    break
        
        return -1 if out == 10**6 else out



