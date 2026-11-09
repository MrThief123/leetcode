'''
961. N-Repeated Element in Size 2N Array
Use a set to track seen elements
Iterate through the array and check if the element has been seen before
Return the first element that is found in the set
'''

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        seen = set()

        for num in nums:
            if num in seen:
                return num
            seen.add(num)
