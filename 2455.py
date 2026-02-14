'''
2455. Average Value of Even Numbers That Are Divisible by Three
Given a 0-indexed integer array nums, return the average value of the even numbers that
are divisible by 3 in nums. The average value of n elements is the sum of the n elements divided (integer division) by n.
Note: The average of 0 elements is considered to be 0.
'''

class Solution:
    def averageValue(self, nums: List[int]) -> int:
        temp = 0
        c = 0

        for i in nums:
            if i %3 == 0 and i%2==0:
                temp += i
                c += 1
        return int(temp/c) if c != 0 else 0