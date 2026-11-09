'''
Remove duplicates from sorted array in-place using two-pointer technique
Maintain a pointer for the position of unique elements
Iterate through the array and when a new unique element is found, place it at the unique
'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # Pointer for the position of unique elements
        unique_index = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[unique_index]:
                unique_index += 1
                nums[unique_index] = nums[i]

        # The number of unique elements is unique_index + 1
        return unique_index + 1