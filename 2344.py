'''
2344. Minimum Operations to Make Array Divisible
Use a counter to count the frequency of each number in nums, 
then check for each number in sorted order if it divides all numbers in numsDivide. 
If it does, return the count of that number in nums. 
If not, keep adding the counts until you find a number that divides all numbers 
in numsDivide or you exhaust all possibilities.
'''

class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        from collections import Counter

        counts = Counter(nums)

        numsDivide = list(set(numsDivide))

        out = 0

        possible = sorted([i for i in counts.keys() if i <= min(numsDivide)])

        for i in possible:
            p = True
            for j in numsDivide:
                if j%i != 0:
                    p = False
                    break
  
            if p:
                return out
            else:
                out += counts[i]

        return -1
