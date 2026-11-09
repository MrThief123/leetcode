'''
2150. Find All Lonely Numbers in the Array
Create hash map of all numbers
'''

class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        from collections import Counter

        counts = Counter(nums)
        out = []

        for num in nums:
            if num+1 not in counts and num-1 not in counts and counts[num] == 1:
                out.append(num)

        return out