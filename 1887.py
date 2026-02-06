'''
1887. Reduction Operations to Make the Array Elements Equal
Medium
Count the number of unique elements and their positions to calculate the total operations needed.
'''

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        temp = sorted(list(set(nums)))
        out = 0
        mydict = {}

        for i, n in enumerate(temp):
            mydict[n] = i

        for i in nums:
            out += mydict[i]

        return out