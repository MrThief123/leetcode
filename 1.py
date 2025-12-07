'''
Iterate through the list of numbers
Use a hash map to store the indices of the numbers we have seen so far.
For each number, calculate the difference between the target and the current number.
Check if this difference exists in the hash map. If it does, return the indices.
If not, add the current number and its index to the hash map.
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = {}

        for i, num in enumerate(nums):
            difference = target - num

            if difference in mydict:
                return [mydict[difference], i]
            else:
                mydict[num] = i