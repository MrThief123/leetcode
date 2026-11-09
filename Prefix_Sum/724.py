'''
Initialize a prefix sum array to store cumulative sums
Iterate through the nums array to fill the prefix sum array
For each index, calculate the left and right sums using the prefix sum array
Return the index if left and right sums are equal, otherwise return -1
'''

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix_sum = [0 for i in range(len(nums) + 1)]

        for i in range(len(nums)):
            prefix_sum[i+1] = prefix_sum[i] + nums[i]

        for i in range(len(nums)):
            left = prefix_sum[i]
            right = prefix_sum[-1] - prefix_sum[i+1]
            if left == right:
                return i
        return -1
