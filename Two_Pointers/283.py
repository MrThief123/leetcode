''''
Use two-pointer technique to move all zeros to the end of the array
Maintain a left pointer to track the position to place the next non-zero element
Iterate through the array with a right pointer
When a non-zero element is found, swap it with the element at the left pointer and increment
'''

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)

        left = 0

        if n == 1:
            return

        for i in range(n):
            if nums[i] != 0:
                temp = nums[left]
                nums[left] = nums[i]
                nums[i] = temp
                left += 1

        

        