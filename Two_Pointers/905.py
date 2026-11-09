'''
905. Sort Array By Parity
Use a two-pointer approach to partition the array in-place.
One pointer tracks the position to place the next even number.
Iterate through the array, and whenever an even number is found, swap it with the number at the even pointer and increment the pointer.
'''

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left = 0 

        for i in range(len(nums)):
            temp = nums[i]
            if nums[i] % 2 == 0:
                nums[i] = nums[left]
                nums[left] = temp
                left += 1

        return nums