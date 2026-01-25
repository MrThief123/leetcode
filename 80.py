'''
80. Remove Duplicates from Sorted Array II
Use a two-pointer technique to overwrite the input array in place.
Count occurrences of each number and allow at most two duplicates.
'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        from collections import Counter
        count = Counter(nums)

        k = 0

        for i, c in count.items():
            
            for j in range(min(c, 2)):
                nums[k] = i
                k += 1

        return k