'''
Remove all instances of val in nums in-place and return the new length
Iterate through the array and when an element equal to val is found, mark it for removal
After marking, sort the array to move all marked elements to the end
Return the count of elements not equal to val
'''

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        out = len(nums)
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = inf
                out -= 1
                
        
        print(nums.sort())
        return out